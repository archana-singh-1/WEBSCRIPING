import json

with open('task_5.json','r')as f:
    j=json.load(f)
    
d={}
for i in j:
    if i["director"] in d:
        d[i["director"]]+=1
    else:
        d[i["director"]]=1
# print(d)
with open ("7_task.json","w") as f:
    json.dump(d,f,indent=2 )