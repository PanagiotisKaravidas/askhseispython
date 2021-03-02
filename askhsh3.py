import urllib.request
import json
from datetime import date

nums=[]
for i in range (80):#πινακας μετρητων για τους αριθμους 0-79
    nums.append(0)

lst=[]
i=1
today = date.today()#Λαμβανει την συμερινή ημερομηνία
first=date.today().replace(day=i)#Λαμβανει την πρώτη ημερομηνία του μηνα
while first<=today:
    url="https://api.opap.gr/draws/v3.0/1100/draw-date/"+str(first)+"/"+str(first)+"/draw-id"

    r=urllib.request.urlopen(url)#Ανοιγμα url
    html=r.read()#Διαβασμα url
    html=html.decode()
    data=json.loads(html,strict=False)#Ληψη δεδομένων με χρήση json
    i=i+1
    first=date.today().replace(day=i)
    url="https://api.opap.gr/draws/v3.0/1100/"+str(data[0])

    r=urllib.request.urlopen(url)#Ανοιγμα url
    html=r.read()#Ανοιγμα url
    html=html.decode()
    data=json.loads(html,strict=False)#Ληψη δεδομένων με χρήση json
    t=data["winningNumbers"]["list"]

    for a in range(20):
        nums[t[a]-1]=nums[t[a]-1]+1#t[a]-1καθως ο πινακας ειναι 0-79 ενω οι αριθμοι του κινο απο το 1-80

for a in range(80):
    print("Ο αριθμος",a+1,"εμφανίστηκε",nums[a],"φορές")#α+1 καθως ο πινακας ειναι 0-79 ενω οι αριθμοι του κινο απο το 1-80
