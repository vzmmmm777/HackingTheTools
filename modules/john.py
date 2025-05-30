print ("Checking Modules")
print ("If a error use setup.py")
print ("Thank you for use my tool")
import os 
print ("Starting tool")
os.system("")
os.system("sudo apt install john")
os.system("pkg install john")
os.system("apk add john")
os.system("clear")
os.system("figlet john the Ripper")
 
hashes_txt = input("Enter Filer Hash:")

if hashes_txt:
    print ("Found Archive Hash")
    os.system(f"john {hashes_txt}")