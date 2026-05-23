from colorama import Fore
from pathlib import Path


def banner():
    path = Path("assets/banner.txt")

    if path.exists():
        print(Fore.CYAN + path.read_text())


def info(text):
    print(Fore.CYAN + text)


def success(text):
    print(Fore.GREEN + text)


def warning(text):
    print(Fore.YELLOW + text)


def error(text):
    print(Fore.RED + text)