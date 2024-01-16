import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from pymongo import MongoClient
from dotenv import load_dotenv

# url = "https://3dnews.ru"
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
# }
#
# req = requests.get(url, headers=headers)
# src = req.text
# print(src)

# Uncomment the following block if you want to save the HTML content to a file
# with open("3dnews.html", "w", encoding="utf-8") as file:
#     file.write(src)

# Uncomment the following block if you want to read the HTML content from a file
with open("3dnews.html", encoding="utf-8") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

description_tag = soup.find("div", class_="header mainph")
desired_text = description_tag.find("h1").text.strip()
print(desired_text)

# Находим тег <a> с классом "icon"
a_tag = soup.find('a', class_='icon')

# Извлекаем значение атрибута style
style_attribute = a_tag['style']

# Извлекаем URL из значения атрибута style
img_url_relative = style_attribute.split('url(')[1].split(')')[0]

# Преобразуем относительный путь в абсолютный URL
base_url = 'https://3dnews.ru'  # Замените на реальный базовый адрес
img_url_absolute = f'{base_url}{img_url_relative}'

print(img_url_absolute)