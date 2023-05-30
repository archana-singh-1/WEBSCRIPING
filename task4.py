import requests
import json
from bs4 import BeautifulSoup
rel=requests.get("https://www.imdb.com/title/tt0066763/")
soup=BeautifulSoup(rel.content,"html.parser")
con=soup.find('script',type='application/ld+json').text
b=json.loads(con)
dic={}

for i in b:
    dic['name']=b['name']
    dic['director']=[b['director'][0]['name']]
    dic['country']="india"
    dic['language']=b['review']['inLanguage']
    dic['image']=b['image']
    dic['description']=b['description']
    dic['genre']=b['genre']