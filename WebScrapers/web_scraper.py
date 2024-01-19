import os
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from dotenv import load_dotenv
from urllib.parse import urljoin, quote

load_dotenv()

mongodb_uri = os.getenv("MONGODB_URI")
cluster = MongoClient(mongodb_uri)
db = cluster["newsdb"]
collection = db["news"]


def scraper_3dnews():
    url = "https://3dnews.ru"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
    req = requests.get(url, headers=headers)
    src = req.text

    soup = BeautifulSoup(src, "lxml")

    title_tag = soup.find("div", class_="header mainph")
    title_text = title_tag.find("h1").text.strip()

    description_tag = soup.find("div", class_="teaser")
    description_text = description_tag.text.strip()

    a_tag = soup.find('a', class_='icon')
    style_attribute = a_tag['style']
    img_url_relative = style_attribute.split('url(')[1].split(')')[0]

    existing_doc = collection.find_one({"title": title_text})

    if existing_doc is None:
        collection.insert_one({
            "source": "3dnews",
            "title": title_text,
            "text": description_text,
            "image_url": img_url_relative
        })
    else:
        print("The data already exists in the database")


def scraper_habr():
    url = "https://habr.com/ru/articles/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
    req = requests.get(url, headers=headers)
    src = req.text

    soup = BeautifulSoup(src, "lxml")

    title_tag = soup.find("h2", class_="tm-title tm-title_h2")
    title_text = title_tag.text.strip()

    description_tag = soup.find("div", class_="article-formatted-body article-formatted-body article-formatted-body_version-2")
    description_text = description_tag.text.strip()

    img_tags = soup.find("img", class_="tm-article-snippet__lead-image")
    img_url = img_tags['src']

    existing_doc = collection.find_one({"title": title_text})

    if existing_doc is None:
        collection.insert_one({
            "source": "habr",
            "title": title_text,
            "text": description_text,
            "image_url": img_url
        })
    else:
        print("The data already exists in the database")


def scraper_ixbt():
    url = "https://www.ixbt.com/news/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
    req = requests.get(url, headers=headers)
    src = req.text

    soup = BeautifulSoup(src, "lxml")

    title_tag = soup.find("strong")
    title_text = title_tag.text.strip()

    description_tag = soup.find("div", class_="item__text__top")
    description_text = description_tag.text.strip()

    img_tag = soup.find("div", class_="item-image").find("img")

    img_src_relative = img_tag['src']
    base_url = "https://www.ixbt.com/news/"
    img_url = urljoin(base_url, quote(img_src_relative, safe="/:"))

    existing_doc = collection.find_one({"title": title_text})

    if existing_doc is None:
        collection.insert_one({
            "source": "ixbt",
            "title": title_text,
            "text": description_text,
            "image_url": img_url
        })
    else:
        print("The data already exists in the database")


def scraper_overclockers():
    url = "https://overclockers.ru/hardnews/lenta"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
    req = requests.get(url, headers=headers)
    src = req.text

    soup = BeautifulSoup(src, "lxml")

    title_tag = soup.find("div", class_="ui header")
    title_text = title_tag.text.strip()

    description_tag = soup.find("div", class_="description")
    description_text = description_tag.find("p").text.strip()

    img_tag = soup.find("div", class_="al-center").find("img")
    img_src_relative = img_tag['src']
    base_url = "https://overclockers.ru/"
    img_url = urljoin(base_url, img_src_relative)

    existing_doc = collection.find_one({"title": title_text})

    if existing_doc is None:
        collection.insert_one({
            "source": "overclockers",
            "title": title_text,
            "text": description_text,
            "image_url": img_url
        })
    else:
        print("The data already exists in the database")


def scraper_rozetked():
    url = "https://rozetked.me/news"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",}
    req = requests.get(url, headers=headers)
    src = req.text

    soup = BeautifulSoup(src, "lxml")

    title_tag = soup.find("div", class_="post_new-title")
    title_text = title_tag.text.strip()

    description_tag = soup.find("div", class_="post_new__main_box_text")
    description_text = description_tag.text.strip()

    img_tag = soup.select_one('picture img')
    base_url = "https://rozetked.me/news"
    img_url = urljoin(base_url, img_tag['src'])

    existing_doc = collection.find_one({"title": title_text})

    if existing_doc is None:
        collection.insert_one({
            "source": "rozetked",
            "title": title_text,
            "text": description_text,
            "image_url": img_url
        })
    else:
        print("The data already exists in the database")


if __name__ == "__main__":
    scraper_rozetked()
