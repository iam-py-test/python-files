import requests
import subprocess
import os
mirrors = {"porn.txt":"porn.txt","Alternative list formats/acsp_abp.txt":"acsp_abp.txt","anti-cookie+sign up.txt":"anti-cookie+sign up.txt","antimalware.txt":"antimalware.txt","antitypo.txt":"antitypo.txt","Alternative list formats/antimalware_domains.txt":"antimalware_domains.txt"}

if os.path.exists("my_filters_001"):
    os.chdir("my_filters_001")
    subprocess.run("git pull",shell=True)
    os.chdir("..")
else:
    subprocess.run("git clone https://github.com/iam-py-test/my_filters_001.git",shell=True)
if os.path.exists("iam-py-test.github.io"):
    os.chdir("iam-py-test.github.io")
    subprocess.run("git pull",shell=True)
    os.chdir("..")
else:
    subprocess.run("git clone https://github.com/iam-py-test/iam-py-test.github.io.git",shell=True)
for file in mirrors:
    with open("my_filters_001/{}".format(file)) as f:
        f2 = open("iam-py-test.github.io/mirrors/{}".format(mirrors[file]),"w")
        f2.write(f.read())
        f.close()
        f2.close()
os.chdir("iam-py-test.github.io")
subprocess.run("git add .",shell=True)
subprocess.run("git commit -m \"[bot] Update mirrors\"",shell=True)
subprocess.run("git push",shell=True)
os.chdir("..")

        