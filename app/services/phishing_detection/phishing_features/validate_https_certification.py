# 8
# Possible values: -1, 0, 1
from urllib.parse import urlparse
import socket
import ssl

def validate_https_certification(url):
    """
    Summary:
        Validates the HTTPS certification of the website.

    Description: 
        Checks if the website starts with "https://".\n
        The hostname is extracted from the URL.\n
        If the website starts with "https://", a SSL context is created.\n
        A socket is created using the hostname and port 443.\n
        The socket is wrapped with the SSL context.\n
        The certificate is extracted from the socket.\n
        The issuer is extracted from the certificate.\n
        The organization name is extracted from the issuer.\n
        A list of trusted issuers is created.\n
        If the organization name contains a trusted issuer and the website starts with "https://", -1 is returned.\n
        If the organization name contains a trusted issuer and the website does not start with "https://", 0 is returned.\n
        If the organization name does not contain a trusted issuer and the website starts with "https://", 0 is returned.\n
        If the organization name does not contain a trusted issuer and the website does not start with "https://", 1 is returned.\n

    Arguments: 
        url (str): The URL of the website.

    Returns: 
        (int): Either -1, 0 or 1

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and 0 is returned.
    """
    try:
        is_https = url.startswith("https://")

        hostname = urlparse(url).netloc
        issued_by = ""

        if is_https:
            context = ssl.create_default_context()
            with socket.create_connection((hostname, 443)) as sock:
                with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                    certificate = ssock.getpeercert()
            
            issuer = dict(x[0] for x in certificate["issuer"])
            issued_by = issuer.get("organizationName", "")

        trusted_issuers = ["GeoTrust", "GoDaddy", "Network Solutions", "Thawte", "Comodo", "Doster", "VeriSign", "Google"]
        
        if any(trusted_issuer in issued_by for trusted_issuer in trusted_issuers) and is_https:
            return -1
        elif any(trusted_issuer in issued_by for trusted_issuer in trusted_issuers) and not is_https:
            return 0
        elif not any(trusted_issuer in issued_by for trusted_issuer in trusted_issuers) and is_https:
            return 0
        else:
            return 1
    except Exception as e:
        print(f"Error in validate_https_certification: {e}")
        return 0
