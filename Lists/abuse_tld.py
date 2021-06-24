import subprocess
import requests
from publicsuffixlist import PublicSuffixList

psl = PublicSuffixList()

abusetld = {}
req = requests.get("https://raw.githubusercontent.com/iam-py-test/my_filters_001/main/antimalware.txt")

lines = req.text.split("\n")
for line in lines:
    if line.startswith("||") or line.startswith("!") or line == "":
        continue
    domain = line.split("$")[0]
    #print("Domain",domain)
    try:
        abusetld[psl.publicsuffix(domain)] += 1
    except:
        abusetld[psl.publicsuffix(domain)] = 1

for tld in abusetld:
    print("Domains for {}: {}".format(tld,abusetld[tld]))