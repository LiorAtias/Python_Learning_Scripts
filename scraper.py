from urllib.request import urlopen
from datetime import date
import re

# constants
ip = input ("What IP address you wish to search? ")
today = date.today()
d1 = today.strftime("%d/%m/%Y")

# reading the webpage content
link = "https://sslbl.abuse.ch/blacklist/sslipblacklist.csv"
f = urlopen(link)
myfile = f.read()

myfile_rts = myfile.decode('UTF-8')
index=myfile_rts.find(ip)
if index != -1:
    print("Found in:", myfile_rts[index-20:index-1])
else:
    print ("CLEAN IP! date:", d1)