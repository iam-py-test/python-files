import subprocess
import os

def arg():
    try:
        import sys
        return sys.argv[1]
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
        if "##" in line and line.startswith("!") == False:
            if "##+js" in line:
                alt.write("! Unsupported")
                alt.write("\n")
                continue
            alt.write(line)
            alt.write("\n")
        elif "#$#" in line and line.startswith("!") == False:
            alt.write("! Unsupported")
            alt.write("\n")
            continue
        elif line.startswith("||"):
            alt.write("||{}".format(line[2:].split("$")[0]))
            alt.write("\n")
        elif line.startswith("!"):
            alt.write(line)
            alt.write("\n")
        elif line != "" and line.split("$")[0] not in donehosts:
            donehosts.append(line.split('$')[0])
            alt.write("||{}^".format(line.split("$")[0]))
            alt.write("\n")
    alt.close()

os.chdir("my_filters_001")
subprocess.call(["git add ."],shell=True)
subprocess.call(["git commit -m \"[bot] add alt list\""],shell=True)
subprocess.call(["git push"],shell=True)



