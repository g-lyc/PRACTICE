#-*-coding:utf-8-*-

import requests as req
from bs4 import BeautifulSoup

url = "https://github.com/keysona/show-me-the-code"

response = req.get(url=url)

soup = BeautifulSoup(response.content,'lxml')

print(soup.article)
