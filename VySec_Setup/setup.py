try:
    import subprocess
    import re
    import platform
    import time
    import os
    import sys
    from colorama import Fore
    import pyfiglet
except ImportError:
    subprocess.call("pip install colorama", shell=True)
    subprocess.call("pip install pyfiglet")

error_message = Fore.RED
success = Fore.GREEN

try:
    def setup():
        ascii_banner = pyfiglet.figlet_format("VySec Setup")
        print(ascii_banner)
        print(Fore.YELLOW + "\n[+] Setup File Version 1.1.0")
        print(Fore.YELLOW + "\n[+] Setup Build Date : ")
        print(Fore.YELLOW + "\n[+] Detected OS : " + platform.system())
        print(Fore.YELLOW + "\n[+] OS Release : " + platform.release())
        print(Fore.CYAN + "\n[+] Starting Setup, Please wait ... ")
        time.sleep(5)
        start_installation = raw_input("\nAvyukt>: Type y if you want to start installation else n >> ")
        if "y" in start_installation:
            print("\n[+] Starting Installation .... Sit Back and Relax!")
            print(Fore.CYAN + "\n\t[+] Updating Packages using apt-get update")
            os.system("sudo apt-get update")
            print(Fore.CYAN + "\n\t[+] Installing Wine")
            print(Fore.YELLOW + "\n")
            subprocess.call("\n\nsudo apt-get install wine32", shell=True)
            print(Fore.CYAN + "\n\t[+] Installing Python 2.7.14 in Wine")
            print(Fore.YELLOW + "\n")
            subprocess.call("\n\nwine msiexec /i python-2.7.14.amd64.msi", shell=True)
            print(os.getcwd())
            os.chdir("/root/.wine/drive_c/Python27/")
            print(Fore.CYAN + "\n\t[+] Installing PyArmor")
            print(Fore.YELLOW + "\n")
            os.system("\n\nwine python.exe -m pip install pyarmor")
            print(Fore.CYAN + "\n\t[+] Installing PyInstaller")
            print(Fore.YELLOW + "\n")
            os.system("\n\nwine python.exe -m pip install pyinstaller")
            print(success + "\n[+] Success in Installing all pre-requisite, If you face any error while running Avyukt, Run the setup.py again")
            raw_input("[+] Press any key to continue ... ")
            os.system("reset")

        if "n" in start_installation:
            print(error_message + "[+] Quitting setup ..")
except FileNotFoundError:
    print(error_message + "[+] Error while Building setup.py")


setup()
