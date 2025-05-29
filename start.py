
import os
from InquirerPy import prompt
import os
import requests
import requests



questions = [
    {
        "type": "list",
        "message": "choice a tool",
        "choices": ["Nmap", "Hydra", "Nikto", "John The Ripper", "Doxxing"],
        "name": "usedtool"

    }
]


print (f"By:Vex77\n__________________________________________________________\n/                       By:Vex77")




result = prompt(questions)

print ("WARNING: I am not responsible for anything done with this tool, at your own risk.")
print ("________________467935797error90347354289___________________")    


if result['usedtool'] == 'Nmap':
    os.system("")
    os.system("python3 /home/guest/HackingTheSystem/modules/nmap.py")
    os.system("python3 /usr/share/HackingTheSystem/modules/nmap.py")
elif result['usedtool'] == 'Hydra':
    os.system("python3 /home/guest/HackingTheSystem/modules/hydra.py")
    os.system("python3 /usr/share/HackingTheSystem/modules/hydra.py")
elif result['usedtool'] == 'Nikto':
    os.system("python3 /home/guest/HackingTheSystem/modules/nikto.py")
    os.system("python3 /usr/share/HackingTheSystem/modules/nikto.py")
elif result['usedtool'] == 'John The Ripper':
    os.system("python3 /home/guest/HackingTheSystem/modules/john.py")
    os.system("python3 /usr/share/HackingTheSystem/modules/john.py")
elif result['usedtool'] == 'Doxxing':
    os.system("python3 /home/guest/HackingTheSystem/modules/doxxing.py")
    os.system("python3 /usr/share/HackingTheSystem/modules/doxxing.py")




