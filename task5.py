import requests,json
from bs4 import BeautifulSoup
list=[]
with open('2_task.json','r')as f:
    a=json.load(f)
for i in a:
    list.append(i['link'])
    
c=list[:10]

detils=['name','director','image','description','language','genre',]
l1=[]
for j in c:
    rel=requests.get(j)
    soup=BeautifulSoup(rel.content,'html.parser')
    con=soup.find('script',type='application/ld+json').text
    b=json.loads(con)
    dic={}

    for k in b:
        dic['name']=b['name']
        dic['director']=b['director'][0]['name']
        dic['country']="india"
        dic['language']=b['review']['inLanguage']
        dic['image']=b['image']
        dic['description']=b['description']
        dic['genre']=b['genre']
    l1.append(dic)
    

with open("task_5.json","w")as f:
    json.dump(l1,f,indent=8)