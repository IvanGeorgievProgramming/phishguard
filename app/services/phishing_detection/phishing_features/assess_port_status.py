# 11
import socket
from urllib.parse import urlparse
from flask import current_app

def assess_port_status(url):
    legitimate_status = current_app.config["LEGITIMATE_STATUS"]
    suspicious_status = current_app.config["SUSPICIOUS_STATUS"]
    phishing_status = current_app.config["PHISHING_STATUS"]
    
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
                return phishing_status

        return legitimate_status
    except Exception as e:
        print(f"Error in assess_port_status: {e}")
        return suspicious_status

def is_port_open(host, port):
    socket_connection_timeout = current_app.config["SOCKET_CONNECTION_TIMEOUT"]

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(socket_connection_timeout)
            if sock.connect_ex((host, port)) == 0:
                return True
            else:
                return False
    except Exception as e:
        print(f"Error in is_port_open: {e}")
        return False
