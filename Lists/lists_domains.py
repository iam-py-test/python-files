import subprocess
import os

def arg(p=1):
    try:
        import sys
        return sys.argv[p]
    except:
        None

donehosts = []
inputfile = input("Enter the file to parse:")
outputfile = input("Enter the file to output to: ")
if os.path.exists("my_filters_001"):
    os.chdir("my_filters_001")
    subprocess.call(["git pull"],shell=True)
    os.chdir("..")
else:
    subprocess.call(["git clone https://github.com/iam-py-test/my_filters_001.git"],shell=True)
alt = open("my_filters_001/Alternative list formats/{}".format(outputfile),"w")
with open("my_filters_001/{}".format(inputfile)) as f:
    lines = f.read().split("\n")
    for line in lines:
        if line.startswith("||"):
            continue
        elif line.startswith("!"):
            continue
        elif line != "" and line.split("$")[0] not in donehosts:
            donehosts.append(line.split("$")[0])
            if arg() == "--lite":
                try:
                    import socket
                    socket.gethostbyname(line.split("$")[0])
                except:
                    pass
                else:
                    alt.write("{}".format(line.split("$")[0]))
                    alt.write("\n")

            else:
                alt.write("{}".format(line.split("$")[0]))
                alt.write("\n")
    alt.close()

os.chdir("my_filters_001")
subprocess.call(["git add ."],shell=True)
subprocess.call(["git commit -m \"[bot] add alt list\""],shell=True)
subprocess.call(["git push"],shell=True)



