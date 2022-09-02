# import necesary packages

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

print(myfile_rts)


# if statement (brain)
pos=myfile_rts.find(ip)
if (pos>0):
    print("Found in:",myfile_rts[pos-22:pos+len(ip)+5] )

else:
    print("CLEAN IP! date:", d1)