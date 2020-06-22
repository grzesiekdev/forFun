from bs4 import BeautifulSoup
import requests
import math
import re


output = open('output.txt', 'w')
for i in range(1, 70):
    page = requests.get(f'https://www.ceneo.pl/sklepy/lymeherbs.pl-s18843/opinie-{i}')
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.find(class_='js_shop-reviews')
    opinions = result.find_all('div', class_='user-post user-post__card js_store-review')
    for opinion in opinions:
        author = opinion.find('span', class_='user-post__author-name')
        rating = opinion.find('span', class_='user-post__score-count')
        date = opinion.find('span', class_='user-post__published')
        content = opinion.find('div', class_='user-post__text')
        if None in (author, rating, date, content):
            continue
        else:
            if content.find('p'):
                continue
            else:
                author = author.text.strip()
                rating = rating.text.strip()
                date = date.text.strip()
                content = content.text.strip()
        output.write(f'Autor: {author}, ocena: {rating}, data: {date}, treść: {content}\n\n')
    print(f'page no. {i}')
