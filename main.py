import requests
from bs4 import BeautifulSoup
import html

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

movie_titles = list(reversed([html.unescape(movie.getText()) for movie in soup.find_all(name="h3", class_="title")]))
# print(movie_titles)

cleanup = movie_titles[58].split()
cleanup.pop(2)
movie_titles[58] = " ".join(cleanup)
# print(cleanup)
#
# print(movie_titles[58])

for m in movie_titles:
    print(m)

with open(file="./movies.txt", mode="w") as file:
    for movie in movie_titles:
        file.write(f"{movie}\n")
