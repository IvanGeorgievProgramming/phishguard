# 1
# Possible values: -1, 1
import re

def check_ip_address_in_domain(url):
    """
    Summary: 
        Checks if the URL contains an IP address in the domain.

    Description: 
        Creates regular expressions for decimal, hexadecimal and octal IP addresses.\n
        Creates an IP address pattern using the regular expressions.\n
        If the URL contains an IP address in the domain, 1 is returned.\n
        If the URL does not contain an IP address in the domain, -1 is returned.\n

    Arguments: 
        url (str): The URL of the website.

    Returns: 
        (int): Either 1 or -1

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and 0 is returned.
    """
    try:
        decimal_ip = r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
        hex_ip = r"(0x[0-9A-Fa-f]{1,2})"
        octal_ip = r"(0[0-7]{1,3})"

        ip_pattern = (
            rf"(?:(?:{decimal_ip}\.){3}{decimal_ip})" +

            rf"|(?:(?:{hex_ip}\.){3}{hex_ip})" +

            rf"|(?:(?:{octal_ip}\.){3}{octal_ip})" +

            rf"|(?:(?:{decimal_ip}|{hex_ip}|{octal_ip})\." +
                rf"(?:{decimal_ip}|{hex_ip}|{octal_ip})\." +
                rf"(?:{decimal_ip}|{hex_ip}|{octal_ip})\." +
                rf"(?:{decimal_ip}|{hex_ip}|{octal_ip}))"
        )

        if re.search(ip_pattern, url):
            return 1
        else:
            return -1
    except Exception as e:
        print(f"Error in check_ip_address_in_domain: {e}")
        return 0
