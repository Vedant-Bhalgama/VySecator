try:
	import subprocess
	import re
	import time
	import pyfiglet
	from pyarmor.pyarmor import main as call_pyarmor
	from os import system, name
	import sys

except ImportError:
	print("\n[+] Import Error Found!")
	print("\n[+] Pre Requistes were not found! Run the requirements.txt file again!")

def clear_output():
	# for windows 
    if name == 'nt': 
		_ = system('cls')
  
	# for mac and linux(here, os.name is 'posix')
    else: 
		_ = system('clear')

ascii_banner = pyfiglet.figlet_format("VySecator")
print(ascii_banner)

print("VySecator - Program Built for Hackers, By Hackers ;)")
print("Version : 1.1.3")
print("\nGitHub Profile :: https://github.com/Vedant-Bhalgama")
raw_input("\nVySec>: Press any key to continue ")
clear_output()

while True:

	def ask_user_choice():
		banner = pyfiglet.figlet_format("VySec Menu")
		print(banner)
		print("\t(1) Obfuscate Python Script ")
		print("\t(2) Compile .py to EXE")
		print("\t(3) Obfuscate and Compile .py to EXE")
		print("\t(4) Obfuscate and Compile to .py to EXE with icon file")
		print("\t(5) Exit Program")
		print("\nFor EG. >> use 1")
		user_input = raw_input("VySec>: ")

		#Main Functions start from here

		if "use 1" in user_input:
			ask_path = raw_input("\n[+] Please enter script path --> ")
			subprocess.call("pyarmor obfuscate " + ask_path)
			print("\n[+] Scripts were Obfuscated Successfully, Please check the dist folder")
			raw_input("\nVySec>: Press any key to continue ")
			clear_output()

		if "use 2" in user_input:
			ask_path = raw_input("\n[+] Please enter script path --> ")
			subprocess.call("pyinstaller --onefile " + ask_path)
			print("\n[+] Scripts were Compiled Successfully, Please check the dist folder")
			raw_input("\nVySec>: Press any key to continue ")
			clear_output()

		if "use 3" in user_input:
			ask_path = raw_input("\n[+] Please enter script path --> ")
			call_pyarmor(['pack', '-e', '--onefile --noconsole', ask_path])
			print("\n[+] Scripts were Obfuscated and Compiled Successfully, Please check the dist folder")
			raw_input("\nVySec>: Press any key to continue ")
			clear_output()

		if "use 4" in user_input:
			ask_path = raw_input("\n[+] Please enter script path --> ")
			cmd = ['pack', '-e', ' --icon %s --onefile' % "def.ico", ask_path]
			call_pyarmor(cmd)
			raw_input("\nVySec>: Press any key to continue ")
			clear_output()
		if "use 5" in user_input:
			print("\n[+] Shutting Down Program")
			sys.exit()


	ask_user_choice()
