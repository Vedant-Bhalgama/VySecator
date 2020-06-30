import subprocess
import re
from pyarmor.pyarmor import main as call_pyarmor


print("+-+-+-+-+-+-+-+-+-+")
print("|V|y|S|e|c|a|t|o|r|")
print("+-+-+-+-+-+-+-+-+-+")

version = "Version Info : 1.1.0"
print(version)



def obfuscate_and_compile(path):
    print("__________________________")
    print("\t\n[1] Obfuscate Scripts")
    print("\t\n[2] Compile to EXE")
    print("\t\n[3] Obfuscate and Compile to EXE")
    print("\n[+] 3 Is more suggested")
    print("__________________________")
    usr_input = input("\n[+] Please enter your choice >> ")
    if "1" in usr_input:
        usr_input = input("[+] Please provide the path of the script >> ")
        subprocess.call("pyarmor obfuscate " + usr_input)
        print("[+] Success In Obfuscating Scripts")


    if "2" in usr_input:
        usr_input = input("[+] Please provide the path of the script >> ")
        subprocess.call("pyinstaller --onefile " + usr_input)
        print("[+] Success In Compiling Scripts")
        

    if "3" in usr_input:
        usr_input = input("[+] Please provide the path of the script >> ")
        call_pyarmor(['pack', '-e', '--onefile --noconsole', usr_input])
        print("\n[+] Success In Compiling the Obfuscated Script")


obfuscate_and_compile("")
