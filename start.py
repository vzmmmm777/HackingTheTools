
import os
from InquirerPy import prompt
import os
import requests
import requests

os.system("sudo apt install figlet")
os.system("pkg install figlet")
os.system("apk add figlet")


questions = [
    {
        "type": "list",
        "message": "choice a tool",
        "choices": ["Nmap", "Hydra", "Nikto", "John The Ripper", "Doxxing"],
        "name": "usedtool"

    }
]


print (f"By:Vex77\n__________________________________________________________\n/                       By:Vex77")

print ("By:Vex77)


result = prompt(questions)

print ("WARNING: I am not responsible for anything done with this tool, at your own risk.")
print ("________________467935797error90347354289___________________")    


if result['usedtool'] == 'Nmap':
    os.system("python3 nmap.py")
    os.system("python3 /home/guest/HackingTheTools/nmap.py")
    os.system("python3 /usr/share/HackingTheTools/nmap.py")
elif result['usedtool'] == 'Hydra':
    os.system("python3 /home/guest/HackingTheTools/hydra.py")
    os.system("python3 /usr/share/HackingTheTools/hydra.py")
    os.system("python3 hydra.py")
elif result['usedtool'] == 'Nikto'
    os.system("python3 /home/guest/HackingTheTools/nikto.py")
    os.system("python3 /usr/share/HackingTheTools/nikto.py")
    os.system("python3 nikto.py")
elif result['usedtool'] == 'John The Ripper':
    os.system("python3 /home/guest/HackingTheTools/john.py")
    os.system("python3 /usr/share/HackingTheTools/john.py")
    os.system("python3 john.py")
elif result['usedtool'] == 'Doxxing':
    os.system("python3 /home/guest/HackingTheTools/doxxing.py")
    os.system("python3 /usr/share/HackingTheToolsmdoxxing.py")
    os.system("python3 doxxing.py")




