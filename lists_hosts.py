import subprocess
import os

def arg(p=1):
    try:
        import sys
        return sys.argv[p]
    except:
        None


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
            if arg() != "--nocomment":
                alt.write(line.replace("!","#"))
                alt.write("\n")
        elif line != "":
            if arg(2) == "--lite" or arg() == "--lite":
                try:
                    import socket
                    socket.gethostbyname(line.split("$")[0])
                except:
                    pass
                else:
                    alt.write("127.0.0.1 {}".format(line.split("$")[0]))
                    alt.write("\n")
            else:
                alt.write("127.0.0.1 {}".format(line.split("$")[0]))
                alt.write("\n")
    alt.close()

os.chdir("my_filters_001")
subprocess.call(["git add ."],shell=True)
subprocess.call(["git commit -m \"[bot] add alt list\""],shell=True)
subprocess.call(["git push"],shell=True)


