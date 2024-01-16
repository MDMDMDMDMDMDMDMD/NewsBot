import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from pymongo import MongoClient
from dotenv import load_dotenv

# url = "https://overclockers.ru/hardnews/lenta"
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
# }
#
# req = requests.get(url, headers=headers)
# src = req.text
# print(src)

# Uncomment the following block if you want to save the HTML content to a file
# with open("overclockers.html", "w", encoding="utf-8") as file:
#     file.write(src)

# Uncomment the following block if you want to read the HTML content from a file
with open("overclockers.html", encoding="utf-8") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

card_titles = soup.find("div", class_="ui header")
print(card_titles.text.strip())

description_tag = soup.find("div", class_="description")
desired_text = description_tag.find("p").text.strip()
print(desired_text)

img_tag = soup.find("div", class_="al-center").find("img")
img_src_relative = img_tag['src']
base_url = "https://overclockers.ru/"
img_src_full = urljoin(base_url, img_src_relative)
print(img_src_full)