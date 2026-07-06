import nltk 
nltk.download('punkt_tab') 
 
from nltk import word_tokenize
from nltk.util import trigrams

text = ("i am your best friend always and forever")

for t in trigrams(word_tokenize(text)):
    print(t)
