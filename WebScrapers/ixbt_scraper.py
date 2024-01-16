import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from pymongo import MongoClient
from dotenv import load_dotenv

# url = "https://www.ixbt.com/news/"
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
# }
#
# req = requests.get(url, headers=headers)
# src = req.text
# print(src)

# Uncomment the following block if you want to save the HTML content to a file
# with open("ixbt.html", "w", encoding="utf-8") as file:
#     file.write(src)

# Uncomment the following block if you want to read the HTML content from a file
with open("ixbt.html", encoding="utf-8") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

card_titles = soup.find("strong")
print(card_titles.text)

card_titles = soup.find("div", class_="item__text__top")
print(card_titles.text)

img_tag = soup.find("div", class_="item-image").find("img")


img_src_relative = img_tag['src']  # Извлекаем относительную ссылку на изображение
base_url = "https://www.ixbt.com/news/"  # Замените "https://www.example.com" на ваш базовый URL
img_src_full = urljoin(base_url, img_src_relative)  # Объединяем относительный путь с базовым URL
print(img_src_full)