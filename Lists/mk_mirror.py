import requests
import os
import subprocess
listtomirror = input("Enter the list to mirror: ")
mirrorname = input("Enter the name of the mirror: ")
req = requests.get(listtomirror)
if os.path.exists("iam-py-test.github.io"):
    os.chdir("iam-py-test.github.io")
    subprocess.call(["git pull"],shell=True)
    os.chdir("..")
else:
    subprocess.call(["git clone https://github.com/iam-py-test/iam-py-test.github.io.git"],shell=True)
with open("iam-py-test.github.io/mirrors/{}".format(mirrorname),"w") as f:
    f.write(req.text)
    f.close()
os.chdir("iam-py-test.github.io")
subprocess.call("git add .",shell=True)
subprocess.call("git commit -m \"[bot] Update mirror\"",shell=True)
subprocess.call("git push",shell=True)