import requests 
from bs4 import BeautifulSoup
import json
req = requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
soup=BeautifulSoup(req.content,'html.parser')
print(soup.prettify())
movies=soup.find('tbody',class_='lister-list').find_all('tr')
name_list=[]
year_list=[]
dic=[]
link_url=[]
for movie in movies:
        list={"movie":"","position":"","rating":"","year":"","link":""}
        name=movie.find('td',class_='titleColumn').a.text
        position=movie.find('td',class_='titleColumn').get_text(strip=True)
        year=movie.find('td',class_='titleColumn')
        # year_list.append(year)
   
        rating=movie.find('td',class_='ratingColumn imdbRating').strong.text
        link=movie.find('td',class_='titleColumn').a['href']
        movie_link="https://www.imdb.com"+link
               
        # link_url.append(movie_link)
        list["movie"]=name
        list["position"]=position
        list["rating"]=rating
        list["link"]=movie_link
        name_list.append(list)
        dic.append(list)
with open("task2 .json","w")as f:
    json.dump(dic,f,indent=8)