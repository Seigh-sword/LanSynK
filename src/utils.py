import random
import socket


def generate_lan_id():
    return random.randint(1000, 9999)


def get_hostname():
    return socket.gethostname()


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]

    finally:
        s.close()

    return ip