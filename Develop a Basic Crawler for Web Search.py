Practical 7: Develop a Basic Crawler for Web Search

command prompt : pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

key = input("Enter Keyword: ")
url = "https://www.bing.com/search?q=" + key

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

for i in soup.select("li.b_algo h2 a"):
    print(i.text)
    print(i["href"])
