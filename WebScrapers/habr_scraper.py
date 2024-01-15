import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from pymongo import MongoClient
from dotenv import load_dotenv

# url = "https://habr.com/ru/articles/"
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
# }
#
# req = requests.get(url, headers=headers)
# src = req.text
# print(src)

# Uncomment the following block if you want to save the HTML content to a file
# with open("habr.html", "w", encoding="utf-8") as file:
#     file.write(src)

# Uncomment the following block if you want to read the HTML content from a file
with open("habr.html", encoding="utf-8") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

card_titles = soup.find("h2", class_="tm-title tm-title_h2")
print(card_titles.text)

card_titles = soup.find("div", class_="article-formatted-body article-formatted-body article-formatted-body_version-2")
print(card_titles.text)

img_tags = soup.find("img", class_="tm-article-snippet__lead-image")
img_src_list = img_tags['src']
print(img_src_list)