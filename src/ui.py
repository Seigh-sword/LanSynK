from colorama import Fore
from pathlib import Path


def banner():
    banner_path = Path("assets/banner.txt")

    if banner_path.exists():
        print(Fore.CYAN + banner_path.read_text())


def info(text):
    print(Fore.CYAN + text)


def success(text):
    print(Fore.GREEN + text)


def warning(text):
    print(Fore.YELLOW + text)


def error(text):
    print(Fore.RED + text)