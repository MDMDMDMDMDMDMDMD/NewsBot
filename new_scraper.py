import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from pymongo import MongoClient
from dotenv import load_dotenv

url = "https://habr.com/ru/articles/top/daily/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}

req = requests.get(url, headers=headers)
src = req.text
print(src)