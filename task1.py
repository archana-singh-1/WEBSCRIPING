import requests
from bs4 import BeautifulSoup

url=("https://www.imdb.com/india/top-rated-indian-movies/")
page=requests.get(url)
soup=BeautifulSoup(page.text,'html.parser')
scraped_movie=soup.find_all('td',class_="titleColumn")
scraped_ratings=soup.find_all('td',class_="titleColumn")
    
movie_name=[]
for movie in scraped_movie:
    movie=movie.get_text().replace("\n","")
    movie_name.append(movie)
    
    
scraped_ratings=soup.find_all(class_="ratingColumn imdbRating")
rating=[]

for ratings in scraped_ratings:
    ratings=ratings.get_text().replace("\n","")
    rating.append(ratings)
    # print(rating)
    i=0
while i<len(movie_name):
    print(movie_name[i],"=",rating[i])
    i=i+1