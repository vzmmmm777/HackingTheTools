print ("Checking Modules")
print ("If a error use setup.py")
print ("Thank you for use my tool")
print ("Starting Brute Force")

import os
os.system("git clone https://github.com/sherlock-project/sherlock && cd sherlock && pip install sherlock-project --break-system-packages")
os.system("clear")
os.system("figlet sherlock")

target_username = input("Enter Username Target:")

print (f"results of doxxing with name {target_username}:")
print ("wait 1 min...")
os.system(f"sherlock {target_username}")
print (f"End Doxxing For {target_username}")