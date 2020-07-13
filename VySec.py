import subprocess
import re
import time
import pyfiglet
from pyarmor.pyarmor import main as call_pyarmor
from os import system, name

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
print("Version : 1.1.2")
print("\nCHANGELOGS --> ADDED PYTHON VERSION 2 SUPPORT, FIXED BUGS")
time.sleep(5)
clear_output()


def ask_user_choice():
	print("\n")
	print("--------------------------------------------")
	print("\t(1) Obfuscate Python Script")
	print("\t(2) Compile .py to EXE")
	print("\t(3) Obfuscate and Compile .py to EXE")
	print("\nFor EG. >> use 1")
	print("--------------------------------------------")
	user_input = raw_input("{+} Enter your choice >> ")

	#Main Functions start from here

	if "use 1" in user_input:
		clear_output()
		ask_path = raw_input("[+] Please enter script path --> ")
		subprocess.call("pyarmor obfuscate " + ask_path)
		print("[+] Scripts were Obfuscated Successfully, Please check the dist folder")


	if "use 2" in user_input:
		clear_output()
		ask_path = raw_input("[+] Please enter script path --> ")
		subprocess.call("pyinstaller --onefile " + ask_path)
		print("[+] Scripts were Compiled Successfully, Please check the dist folder")


	if "use 3" in user_input:
		clear_output()
		ask_path = raw_input("[+] Please enter script path --> ")
		call_pyarmor(['pack', '-e', '--onefile --noconsole', ask_path])
		print("[+] Scripts were Obfuscated and Compiled Successfully, Please check the dist folder")


ask_user_choice()


