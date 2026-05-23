import argparse

from colorama import init

from src.ui import banner

from src.host import start_host

from src.discovery import discover_sessions

init(autoreset=True)

banner()

parser = argparse.ArgumentParser()

parser.add_argument(
    "command",
    nargs="?"
)

parser.add_argument(
    "target",
    nargs="?"
)

args = parser.parse_args()

if args.command == "host":
    start_host(args.target or ".")

elif args.command == "ls":
    discover_sessions()

else:
    print("Usage:\n")

    print("Host current folder:")
    print("host .\n")

    print("Find sessions:")
    print("ls")