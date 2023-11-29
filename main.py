import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

movie_titles = [movie.getText() for movie in soup.find_all(name="h3", class_="title")]
print(movie_titles)
