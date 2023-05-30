import requests
import json
from bs4 import BeautifulSoup
rel=requests.get("https://www.imdb.com/title/tt0066763/")
soup=BeautifulSoup(rel.content,"html.parser")
con=soup.find('script',type='application/ld+json').text
b=json.loads(con)
dic={}
for key in b:
    if key=="url":
        p=b[key]
        dic['id']=p
with open("task_8.json","w")as f:
    json.dump(dic,f,indent=2)