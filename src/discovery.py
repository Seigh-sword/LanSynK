import socket
import json

from config import DISCOVERY_PORT

from ui import (
    success,
    info
)


def discover_sessions():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.bind(("", DISCOVERY_PORT))

    success("\n[SEARCHING FOR SESSIONS]\n")

    seen = set()

    while True:
        data, addr = sock.recvfrom(4096)

        try:
            session = json.loads(data.decode())

            unique = (
                f"{session['id']}"
                f"-{session['ip']}"
            )

            if unique not in seen:
                seen.add(unique)

                info(
                    f"[{session['id']}] "
                    f"{session['hostname']}"
                )

                print(
                    f"Folder : {session['folder']}"
                )

                print(
                    f"IP     : {session['ip']}\n"
                )

        except:
            pass