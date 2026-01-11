import requests
import socket

class HtkNetworkCheck:
    @staticmethod
    def is_connected(host="8.8.8.8", port=53, timeout=5):
        try:
            if host and port:
                socket.create_connection((host, port), timeout=timeout)
            else:
                requests.get("http://www.google.com", timeout=timeout)
            return True
        except (socket.error, requests.ConnectionError):
            return False
