from bs4 import BeautifulSoup

import requests
import sys

url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text, features="html.parser")
tr = soup.findChildren("tr")
tr = iter(tr)
next(tr)

print("Title \t Year\t Rating")
# for movie in tr:
#     # print(movie)
#     title = movie.find('td', {'class': 'titleColumn'}).find('a').contents[0]
#     year = movie.find('td', {'class': 'titleColumn'}).find('span', {'class': 'secondaryInfo'}).contents[0]
#     rating = movie.find('td', {'class': 'ratingColumn imdbRating'}).find('strong').contents[0]
#     row = title + ' - ' + year + ' ' + ' ' + rating
#     print(row)

movielist = []
movielist2 = []
for movie in tr:
    # print(movie)
    title = movie.find('td', {'class': 'titleColumn'}).find('a').contents[0]
    year = movie.find('td', {'class': 'titleColumn'}).find('span', {'class': 'secondaryInfo'}).contents[0]
    rating = movie.find('td', {'class': 'ratingColumn imdbRating'}).find('strong').contents[0]
    row = title + ' - ' + year + ' ' + ' ' + rating
    movielist1 = [title,year,rating]
    movielist2.append(movielist1)   ### Create list of list

print(movielist2.sort())