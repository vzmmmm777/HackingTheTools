print ("Checking Modules")
print ("If a error use setup.py")
print ("Thank you for use my tool")

import os
target_site = input("Enter Site Target:")
os.system(f"sudo apt install nmap && clear && figlet nmap && nmap {target_site}")