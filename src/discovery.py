import socket
import json

from config import DISCOVERY_PORT

from ui import (
    success,
    info
)


def discover_sessions():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_REUSEADDR,
        1
    )

    sock.bind(("", DISCOVERY_PORT))

    success("\n[SEARCHING FOR SESSIONS]\n")

    seen = set()

    while True:
        data, addr = sock.recvfrom(4096)

        try:
            print("Packet received")

            session = json.loads(
                data.decode()
            )

            unique = (
                f"{session['id']}"
                f"-"
                f"{session['ip']}"
            )

            if unique not in seen:
                seen.add(unique)

                info(
                    f"\n[{session['id']}] "
                    f"{session['hostname']}"
                )

                print(
                    f"Folder : {session['folder']}"
                )

                print(
                    f"IP     : {session['ip']}"
                )

        except Exception as e:
            print("Error:", e)