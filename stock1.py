import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get(
	url="https://en.wikipedia.org/wiki/Toronto_Stock_Exchange",
)
soup = BeautifulSoup(response.content, 'html.parser')

website = soup.select(".toccolours a")
links = []
for link in website:
    links.append(link.get('href'))

out = requests.get("https://en.wikipedia.org{}".format(links[2]))
htmlcode = BeautifulSoup(out.content,'html.parser')
var1 = soup.find("table")
print(var1)
