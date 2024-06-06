import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
# decoding required due to crash at title 59
response.encoding = 'utf-8'
website_html_decode = response.content.decode('utf-8')

soup = BeautifulSoup(website_html_decode, "html.parser")
# print(soup.prettify())
# print(soup.text)

movies_scraped = soup.find_all(name="h3", class_="title")
# print(movies_scraped)

movies_titles = [movie.getText() for movie in movies_scraped]

# can use [::-1] on a list to reverse the list
# can use .reverse() to revers the list
# print(movies_titles[::-1])

movies = movies_titles[::-1]
print(movies)
with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
