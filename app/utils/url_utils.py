import base64
from urllib.parse import urlparse, urljoin

def generate_route_name(url):
    try:
        encoded_url = base64.urlsafe_b64encode(url.encode()).decode()

        return encoded_url
    except Exception as e:
        print(f"Error generating route name: {e}")
        return None

def reconstruct_route_name(encoded_route_name):
    try:
        decoded_bytes = base64.urlsafe_b64decode(encoded_route_name.encode())
        
        return decoded_bytes.decode()
    except Exception as e:
        print(f"Error reconstructing url: {e}")
        return None

def is_same_domain(url1, url2):
    try:
        domain_name1 = urlparse(url1).netloc
        domain_name2 = urlparse(url2).netloc

        if domain_name1 == domain_name2:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error checking if urls are from the same domain: {e}")
        return False

def is_relative_link(url):
    try:
        parsed_url = urlparse(url)
        if parsed_url.scheme == "" and parsed_url.netloc == "":
            return True
        else:
            return False
    except Exception as e:
        print(f"Error checking if url is relative: {e}")
        return False
