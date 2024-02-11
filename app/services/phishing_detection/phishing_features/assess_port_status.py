# 11
import socket
from urllib.parse import urlparse

def assess_port_status(url):
    """
    Summary: 
        Assess the status of some important ports.

    Description: 
        A dictionary containing the important ports and their expected status is created.\n
        For each port, a connection is established to the given host and port.\n
        If the connection is successful and the status is not as expected, 1 is returned.\n
        If the connection is unsuccessful and the status is not as expected, 1 is returned.\n
        If the connection is successful and the status is as expected, 0 is returned.\n
        If the connection is unsuccessful and the status is as expected, 0 is returned.\n

    Arguments: 
        url (str): The URL of the website.

    Returns: 
        (int): Either 0 or 1

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and 0.5 is returned.
    """
    try:
        domain = urlparse(url).netloc

        important_ports = {
            21: "close",   # FTP
            22: "close",   # SSH
            23: "close",   # Telnet
            80: "open",    # HTTP
            443: "open",   # HTTPS
            445: "close",  # SMB
            1433: "close", # MSSQL
            1521: "close", # ORACLE
            3306: "close", # MySQL
            3389: "close", # Remote Desktop
        }

        for port, status in important_ports.items():
            if is_port_open(domain, port) != (status == "open"):
                return 1

        return 0
    except Exception as e:
        print(f"Error in assess_port_status: {e}")
        return 0.5

def is_port_open(host, port):
    """
    Summary: 
        Check if a port is open or not.

    Description: 
        A socket is created and a connection to the given host and port is established.
        If the connection is successful, True is returned.
        If the connection is unsuccessful, False is returned.

    Arguments: 
        host (str): The host to connect to.
        port (int): The port to connect to.

    Returns: 
        (bool): True if the connection was successful, False otherwise.

    Exceptions: 
        In case of an exception during the execution of the function, an error message is printed to the console and False is returned.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            if sock.connect_ex((host, port)) == 0:
                return True
            else:
                return False
    except Exception as e:
        print(f"Error in is_port_open: {e}")
        return False
