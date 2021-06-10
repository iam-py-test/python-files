import requests
from random import choice
import subprocess
import os

def domainExists(domain):
    try:
        import socket
        ip = socket.gethostbyname(domain)
    except:
        return False
    else:
        return True
def alreadyExists(domain=""):
    try:
        with open("my_filters_001/porn_auto.txt") as f:
            return domain in f.read()
    except:
        return False

if os.path.exists("my_filters_001"):
    os.chdir("my_filters_001")
    subprocess.call(["git pull"],shell=True)
    os.chdir("..")
else:
    subprocess.call(["git clone https://github.com/iam-py-test/my_filters_001.git"],shell=True)

for t in range(0,28):
    domain = ""
    r = choice([2,3,4,5,6,7])
    for t2 in range(1,r):
        domain += choice(["porn","teen","sex","sexy","slut","fuck","preg","belly","boobs","teens","men","cock","pussy","prego","porno","xxx","girl","prego"])
    domain = "{}.{}".format(domain,choice(["com","net","xxx","xyz","sex"]))
    if domainExists(domain) and alreadyExists(domain) == False:
        print("Adding {}".format(domain))
        with open("my_filters_001/porn_auto.txt","a") as f:
            f.write("\n")
            f.write(domain)
            f.close()
os.chdir("my_filters_001")
subprocess.call(["git add ."],shell=True)
subprocess.call(["git commit -m \"[bot] add random porn domains\""],shell=True)
subprocess.call(["git push"],shell=True)

