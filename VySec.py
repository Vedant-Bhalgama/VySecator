import subprocess
import re
import time
import pyfiglet
from pyarmor.pyarmor import main as call_pyarmor


ascii_banner = pyfiglet.figlet_format("VySecator")
print(ascii_banner)

print("VySecator - Program Built for Hackers, By Hackers ;)")
print("Version : 1.1.2")
print("\nCHANGELOGS --> ADDED PYTHON VERSION 2 SUPPORT")
time.sleep(5)
subprocess.call("cls", shell=True)


def ask_user_choice():
	print("______________________________________________")
	print("\t(1) Obfuscate Python Script                |")
	print("\t(2) Compile .py to EXE                     |")
	print("\t(3) Obfuscate and Compile .py to EXE       |")
	print("\nFor EG. >> use 1                           |")
	print("_____________________________________________|")
	user_input = raw_input("{+} Enter your choice >> ")

	#Main Functions start from here

	if "use 1" in user_input:
		subprocess.call("clear", shell=True)
		subprocess.call("cls", shell=True)
		ask_path = raw_input("[+] Please enter script path --> ")
		subprocess.call("pyarmor obfuscate " + ask_path)
		print("[+] Scripts were Obfuscated Successfully, Please check the dist folder")

	if "use 2" in user_input:
		subprocess.call("cls", shell=True)
		subprocess.call("clear", shell=True)
		ask_path = raw_input("[+] Please enter script path --> ")
		subprocess.call("pyinstaller --onefile " + ask_path)
		print("[+] Scripts were Compiled Successfully, Please check the dist folder")

	if "use 3" in user_input:
		subprocess.call("cls", shell=True)
		subprocess.call("clear", shell=True)
		ask_path = raw_input("[+] Please enter script path --> ")
		call_pyarmor(['pack', '-e', '--onefile --noconsole', ask_path])
		print("[+] Scripts were Obfuscated and Compiled Successfully, Please check the dist folder")


ask_user_choice()

