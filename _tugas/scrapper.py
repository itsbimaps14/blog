import requests
import datetime
import json

article = {}
all = []

from bs4 import BeautifulSoup

page = requests.get("https://www.republika.co.id/")

obj = BeautifulSoup(page.text, "html.parser")

for headline in obj.find_all('div', class_='conten1'):
    tmpa = headline.find('h1').text
    tmpb = headline.find('h2').text
    date = datetime.datetime.now()
    today = date.strftime("%A")+", "+date.strftime("%d")+" "+date.strftime("%B")+" "+date.strftime("%Y")
    tmpc = today

    article['kateg'] = tmpa
    article['judul'] = tmpb
    article['waktu'] = tmpc

    all.append(dict(article))

with open("headline.json", "w") as write_file:
    json.dump(all, write_file, indent=4)