Practical 9: Deep Search Implementation to Detect Plagiarism in Documents Online

command prompt: pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup
from difflib import SequenceMatcher

text = input("Enter Text: ")

page = requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)")
soup = BeautifulSoup(page.text, "html.parser")

web = soup.get_text()

s = SequenceMatcher(None, text, web).ratio()*100

print("Similarity:", round(s,2), "%")

if s>20:
    print("Possible Plagiarism")
else:
    print("No Plagiarism")
