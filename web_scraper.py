import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from pymongo import MongoClient
from dotenv import load_dotenv

# url = "https://rozetked.me/news"
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
# }
#
# req = requests.get(url, headers=headers)
# src = req.text

# # Uncomment the following block if you want to save the HTML content to a file
# with open("index.html", "w", encoding="utf-8") as file:
#     file.write(src)
#
# # Uncomment the following block if you want to read the HTML content from a file
with open("index.html", encoding="utf-8") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

card_titles = soup.find("div", class_="post_new-title")
print(card_titles.text)


img_tag = soup.select_one('picture img')

# Получить базовый URL
base_url = "https://rozetked.me/news"  # Замените на ваш базовый URL

# Используйте urljoin для преобразования относительного URL в абсолютный
image_url = urljoin(base_url, img_tag['src'])

print("Ссылка на картинку:", image_url)