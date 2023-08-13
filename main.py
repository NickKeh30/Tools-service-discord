import os
from colorama import init, Fore


init(autoreset=True)

missing = []

try:
    import requests
except ImportError:
    missing.append("requests")

try:
    import tls_client
except ImportError:
    missing.append("tls-client")

try:
    import ipinfo
except ImportError:
    missing.append("ipinfo")

try:
    import colorama
except ImportError:
    missing.append("colorama")

try:
    import discord
except ImportError:
    missing.append("discord")

try:
    from termcolor import colored
except ImportError:
    missing.append("termcolor")

try:
    from discord import commands
except ImportError:
    pass

for lib in missing:
    os.system(f"pip install {lib}")

if len(missing) > 0:
    os.system("python main.py")
else:
    print(Fore.RED + """
████████╗░█████╗░░█████╗░██╗░░░░░███████╗
╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░╚════██║
░░░██║░░░██║░░██║██║░░██║██║░░░░░░░███╔═╝
░░░██║░░░██║░░██║██║░░██║██║░░░░░██╔══╝░░
░░░██║░░░╚█████╔╝╚█████╔╝███████╗███████╗
░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚══════╝
    Nick. milkmanriot. FREE VERSION INCLUDES DDOS
    
    [1] DDOS | WARNING
    [2] PORT SCANNER
    """)

    choice = input("Enter your choice: ")
    if choice == "1":
        print("Running fun.py...")
        os.system("python fun.py")
    elif choice == "2":
        print("Running port.py...")
        os.system("python port.py")
    else:
        print("Invalid choice. Please select a valid option.")
