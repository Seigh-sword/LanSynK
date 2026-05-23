import argparse

from colorama import init

from ui import banner

from host import start_host
from discovery import discover_sessions

init(autoreset=True)

banner()

parser = argparse.ArgumentParser()

parser.add_argument("-host", nargs="?")
parser.add_argument("-ls", action="store_true")

args = parser.parse_args()

if args.host:
    start_host(args.host)

elif args.ls:
    discover_sessions()

else:
    print("Usage:")
    print("  python src/main.py -host .")
    print("  python src/main.py -ls")