# Kali Linux Version for VySecator
# Version 1.1.5
# Modifying the code doesn't make it yours ;)
# Python Version 2.7.14
# Make sure to run the setup.py before starting the program,


try:
	import subprocess
	import re
	import time
	import pyfiglet
	from os import system, name
	import sys
	import os
	from colorama import Fore

except ImportError:
	print("\n[+] Import Error!")
	print("\n[+] Pre Requistes were not found! Run the setup.py file again!")

ascii_banner = pyfiglet.figlet_format("VySecator")
print(ascii_banner)

print(Fore.RED + "VySecator - Program Built for Hackers, By Hackers ;)")
print("Version : 1.1.7")
print("Supported OS : Kali Linux")
print("GitHub Profile :: https://github.com/Vedant-Bhalgama")
raw_input(Fore.WHITE + "\nVySec>: Press enter to continue ")
os.system("clear")

while True:

	def ask_user_choice():
		while True:
			print(Fore.WHITE)
			banner = pyfiglet.figlet_format("VySec Menu")
			print(banner)
			print(Fore.RED + "\t(1) Obfuscate Python Script ")
			print(Fore.RED + "\t(2) Compile .py to EXE")
			print(Fore.RED + "\t(3) Obfuscate and Compile .py to EXE")
			print(Fore.RED + "\t(4) Exit Program")
			print(Fore.RED + "\nFor EG. >> use 3")
			user_input = raw_input(Fore.WHITE + "\nVySec>: ")

			# Main Functions start from here

			if "use 1" in user_input:
				ask_path = raw_input("\nVySec>: Please enter script path --> ")
				subprocess.call(['wine', '/root/.wine/drive_c/Python27/Scripts/pyarmor.exe', 'obfuscate', ask_path])

			if "use 2" in user_input:
				ask_icon = raw_input("\nVySec>: Do you want to add icon to EXE? y/n >> ")
				if "y" in ask_icon:
					ask_path = raw_input("\nVySec>: Please enter script path --> ")
					ask_icon_path = raw_input("\nVySec>: Please enter icon path (Only .ico files are supported) --> ")
					subprocess.call(['wine', '/root/.wine/drive_c/Python27/Scripts/pyinstaller', '--onefile', '--noconsole', '--icon', ask_icon_path, ask_path])

				if "n" in ask_icon:
					ask_path = raw_input("\nVySec>: Please enter script path --> ")
					subprocess.call(['wine', '/root/.wine/drive_c/Python27/Scripts/pyinstaller.exe', '--noconsole', '--onefile', ask_path])

			if "use 3" in user_input:
				ask_icon = raw_input("\nVySec>: Do you want to add icon to EXE? y/n >> ")

				if "y" in ask_icon:
					ask_path = raw_input("\nVySec>: Please enter script path --> ")
					ask_icon_path = raw_input("\nVySec>: Please enter icon path (Only .ico files are supported) --> ")
					subprocess.call(['wine', '/root/.wine/drive_c/Python27/Scripts/pyarmor.exe', 'pack', '-e', '--onefile --noconsole --icon %s' % ask_icon_path, ask_path])

				if "n" in ask_icon:
					ask_path = raw_input("\nVySec>: Please enter script path --> ")
					subprocess.call(['wine', '/root/.wine/drive_c/Python27/Scripts/pyarmor.exe', 'pack', '-e', '--onefile --noconsole', ask_path])

			if "use 4" in user_input:
				print("\nVySec>: Shutting Down Program")
				sys.exit()

			raw_input(Fore.WHITE + "\nVySec:> Press enter to continue")
			os.system("clear")


	ask_user_choice()
