import requests
from bs4 import BeautifulSoup, SoupStrainer
url = input("Enter the url to run a deep scan on: ")
file = input("Enter the file to save the results to: ")
req = requests.get(url,headers={"accept":"text/html,application/xhtml+xml;q=0.9,image/webp,*/*,q=0.8","accept-encoding":"gzip, deflate, br","accept-language":"en-US,en;q=0.5","DNT":"1","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"})
soup = BeautifulSoup(req.text,features="html.parser")
for iframe in soup.find_all("iframe"):
    with open(file,"a") as f:
        f.write("\n{}".format(iframe.get("src")))
        f.close()
for img in soup.find_all("img"):
    with open(file,"a") as f:
        f.write("\n{}".format(img.get("src")))
        f.close()
for script in soup.find_all("script"):
    with open(file,"a") as f:
        f.write("\n{}".format(script.get("src")))
        f.close()
for a in soup.find_all("a"):
    with open(file,"a") as f:
        f.write("\n{}".format(a.get("href")))
        f.close()
print(req.text)