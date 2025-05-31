
import os
from InquirerPy import prompt
import os
import requests
import requests
os.system("apt update && apt upgrade")
os.system("pkg update && pkg upgrade")
os.system("apk update && apk update")
os.system("sudo apt install figlet")
os.system("pkg install figlet")
os.system("apk add figlet")



questions = [
    {
        "type": "list",
        "message": "choice a tool",
        "choices": ["Nmap", "Hydra", "Nikto", "John The Ripper", "__________", "Doxxing-Name Completed Of Victim", "Doxxing search all accounts of a victim"],
        "name": "usedtool"

    }
]


print (f"By:Vex77\n__________________________________________________________\n/                       By:Vex77")

print ("By:discord:vex77, tiktok:vex77, instagram:vex772025")


result = prompt(questions)

print ("WARNING: I am not responsible for anything done with this tool, at your own risk.")
print ("________________467935797error90347354289___________________")    


if result['usedtool'] == 'Nmap':
    os.system("cd modules && python3 nmap.py")
    os.system("python3 /home/guest/HackingTheTools/modules/nmap.py")
    os.system("python3 /usr/share/HackingTheTools/modules/nmap.py")
elif result['usedtool'] == 'Hydra':
    os.system("python3 /home/guest/HackingTheTools/modules/hydra.py")
    os.system("python3 /usr/share/HackingTheTools/modules/hydra.py")
    os.system("cd modules && python3 hydra.py")
elif result['usedtool'] == 'Nikto':
    os.system("python3 /home/guest/HackingTheTool/modules/nikto.py")
    os.system("python3 /usr/share/HackingTheTools/modules/nikto.py")
    os.system("cd modules && python3 nikto.py")
elif result['usedtool'] == 'John The Ripper':
    os.system("python3 /home/guest/HackingTheTools/modules/john.py")
    os.system("python3 /usr/share/HackingTheTools/modules/john.py")
    os.system("cd modules && python3 john.py")
elif result['usedtool'] == 'Doxxing-Name Completed Of Victim':
    os.system("python3 /home/guest/HackingTheTools/modules/doxxing.py")
    os.system("python3 /usr/share/HackingTheTools/modules/doxxing.py")
    os.system("cd modules && python3 doxxing.py")
elif result['usedtool'] == 'Doxxing search all accounts of a victim':
    os.system("python3 /home/guest/HackingTheTools/modules/sherlock.py")
    os.system("python3 /home/guest/HackingTheTools/modules/sherlock.py")
    os.system("cd modules && python3 sherlock.py")
# discord:vex77, tiktok:vex77, instagram:vex772025



