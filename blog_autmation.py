from os import O_APPEND
import bs4
import requests
from bs4 import BeautifulSoup as bs
url = "http://azeezullah.hussnainconsultants.com/index.php"
open_url = requests.get(url)
page = bs(open_url.content, "html.parser")
fin = page.findAll(class_="card-description")
for i in range(len(fin)):
    print(fin[i].text)
open_url.close()