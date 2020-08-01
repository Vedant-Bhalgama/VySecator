# VySecator - A useful tool made for Hackers and By Hackers ;)
**General Info about the tool**
**VySecator Is a tool which can be used to Obfuscate your Python script. The tool comes with 3 Options. Obfuscate Python Script, Compile to EXE, Compile to EXE with Obfuscation.
3rd Options is the most used by Hackers who program their own Malware and want to make it FUD.**
**VySecator uses Wine which makes it possible to generate Windows Executables in Linux**

# Note 

--> My tool doesn't work for MsfVenom Payloads, I will bring a update in Future which will consist of Obfuscating and Compiling MsfVenom Python Payloads also.

# Read the tool article on ZSecurity's Website!

--> https://zsecurity.org/vysecator-a-useful-tool-made-for-hackers-and-by-hackers/


# Update 1.1.6

**--> Added a new feature in option 2 and option 3. Now you can also add your custom icon (.ico) to the EXE.


**--> Fixed Bugs**

# OS Support

--> Linux only (Kali Linux is suggested)

 
# Installation
 --> Use the git clone command for cloning my Repository or simply click on Download as zip
     https://github.com/VySec-Secure/VySecator.git
 
--> After you have the files, Run the setup.py

--> setup.py will install all the dependencies such as wine, PyArmor, PyInstaller and also it will Install Windows Python under wine

![VySecstup](https://user-images.githubusercontent.com/67494275/88782304-0c0cce00-d1ab-11ea-9015-0bfa077022dc.PNG)

![setup](https://user-images.githubusercontent.com/67494275/88782577-6148df80-d1ab-11ea-9627-d008c1aa2f0e.PNG)


# Using the Program
 --> Now In order to run the program, Just run using this command, Also refer to the Screenshot below.
 
 `python ./VySec.py`
 
![Main menu](https://user-images.githubusercontent.com/67494275/88782664-77ef3680-d1ab-11ea-894e-8db597bcdb4d.PNG)

 --> Now you will see 4 options as Follows
 
 --> Now FOR.EG I want to use the 3rd one, The 3rd Option will obfuscate your script first and then Compile it to EXE,
     This is the main Reason why this is very important for Hackers who program their Malwares on their own!
     
 --> In Order to Use any Options just type
 
     use 1
     use 2
     use 3
     use 4
     
 
 --> Now, If you choose option 3 or option 2, It will ask you to add a icon to the EXE. If you want to add a icon, Then type y else n.
 
 --> If you type y, It will first ask you to enter the script path and then it will ask you to enter the icon file path.
 
 **--> ALSO MAKE SURE THE ICON FILE WHICH YOU WANT TO ADD IS IN .ico EXTENSTION**
 
 
![Capture](https://user-images.githubusercontent.com/67494275/89103181-7d5bb380-d42d-11ea-822c-43c0ea074494.PNG)


 --> Now It will start doing the things sit back and relax!
 
 --> After it completes you will see something like this at the end
 
![output](https://user-images.githubusercontent.com/67494275/88783625-a4f01900-d1ac-11ea-845b-daed3b024380.png)
 
--> Now to find the script, You can see in the image above a Blue Line is there, The final EXE will be in that path.

--> See the final path of our test script here.

**WITHOUT ICON**

![Capture](https://user-images.githubusercontent.com/67494275/88783271-30b57580-d1ac-11ea-8e50-137a77c39853.PNG)

**WITH ICON**

**YOU ONLY WILL SEE THE ICON ON THE WINDOWS MACHINE, SO IF YOU DONT SEE THE ICON ON LINUX MACHINE, PLEASE MAKE SURE TO TRANSFER THAT FILE TO WINDOWS MACHINE AND SEE IT.


![Capture](https://user-images.githubusercontent.com/67494275/89103253-04a92700-d42e-11ea-8872-2edc06411e34.PNG)


# Bug and Issue Report
 --> Make sure to report any bugs or issues here -> https://github.com/VySec-Secure/VySecator/issues
 
 --> If no one replies within 48 Hours, Please mail your issue here 

     - - > pentestmadefun@outlook.com
 

# Why removed Windows Version?

**I had to remove the Windows Version because this program is mainly made for Ethical Hackers, 
Which makes it easy for using them in Kali Linux ;)**
      
# What's new in Future Update 1.1.7 ?

**--> I am thinking to add a different option to Obfuscate and Compile MsfVenom Payloads to EXE (Python Payloads)
      
