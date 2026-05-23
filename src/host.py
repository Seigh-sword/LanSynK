import socket
import time
import json

from threading import Thread

from config import (
    DISCOVERY_PORT,
    BROADCAST_INTERVAL
)

from utils import (
    generate_lan_id,
    get_hostname,
    get_local_ip
)

from ui import (
    success,
    info
)


def broadcast_loop(session_data):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_BROADCAST,
        1
    )

    while True:
        message = json.dumps(session_data)

        sock.sendto(
            message.encode(),
            ("255.255.255.255", DISCOVERY_PORT)
        )

        time.sleep(BROADCAST_INTERVAL)


def start_host(folder):
    lan_id = generate_lan_id()

    hostname = get_hostname()
    ip = get_local_ip()

    session_data = {
        "id": lan_id,
        "hostname": hostname,
        "folder": folder,
        "ip": ip
    }

    success("\n[HOST STARTED]\n")

    info(f"Session ID : {lan_id}")
    info(f"Hostname   : {hostname}")
    info(f"Folder     : {folder}")
    info(f"IP Address : {ip}")

    Thread(
        target=broadcast_loop,
        args=(session_data,),
        daemon=True
    ).start()

    info("\nBroadcasting session...\n")

    while True:
        time.sleep(1)