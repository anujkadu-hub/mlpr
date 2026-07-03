Practical 5: Demonstrate Text Mining and Webpage Pre-processing using meta information 
from the web pages (Local/Online). 

command prompt : pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup
import re

page = requests.get("https://www.python.org")
soup = BeautifulSoup(page.text, "html.parser")

for m in soup.find_all("meta"):
    if m.get("content"):
        text = re.sub(r'[^a-zA-Z ]', '', m["content"]).lower()
        tag = m.get("name") or m.get("property")
        if tag:
            print(tag, ":", text)
