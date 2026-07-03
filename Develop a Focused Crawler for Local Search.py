Practical 8: Develop a Focused Crawler for Local Search

command prompt: pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

key = input("Enter Keyword: ").lower()
url = "https://www.bing.com/search?q=" + key

soup = BeautifulSoup(requests.get(url).text, "html.parser")

for i in soup.find_all("a", href=True):
    if key in i.text.lower():
        print(i.text)
        print("https://en.wikipedia.org" + i["href"])
