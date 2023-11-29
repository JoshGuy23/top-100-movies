import requests
from bs4 import BeautifulSoup
import html

# Get the website's html.
response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()
webpage = response.text

# Start the html parser
soup = BeautifulSoup(webpage, "html.parser")

# Get the list of movie rankings starting from 1.
movie_titles = list(reversed([html.unescape(movie.getText()) for movie in soup.find_all(name="h3", class_="title")]))

# print(movie_titles)

# Cleanup the title of a movie whose formatting resulted in errors
cleanup = movie_titles[58].split()
cleanup.pop(2)
movie_titles[58] = " ".join(cleanup)

# print(cleanup)
#
# print(movie_titles[58])

# for m in movie_titles:
#     print(m)

# Write the movie list to a text file.
with open(file="./movies.txt", mode="w") as file:
    for movie in movie_titles:
        file.write(f"{movie}\n")
