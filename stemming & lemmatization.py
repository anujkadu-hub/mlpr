import nltk
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 
ps=PorterStemmer() 
words=["programs","programer","programing","programmers"] 
for w in words: 
  print(w,":",ps.stem(w))
from nltk.tokenize import word_tokenize 
ps=PorterStemmer() 
sentence="programmers program with programing languages" 
words=word_tokenize(sentence) 
for w in words: 
  print(w,":",ps.stem(w)) 
 
nltk.download('wordnet') 
from nltk.stem import WordNetLemmatizer 
 
Lemma=WordNetLemmatizer() 
 
words=["rocks","corpora","better","best","worst"] 
 
for w in words: 
  print(w,":",Lemma.lemmatize(w)) 
print("better:", Lemma.lemmatize("better",pos="a"))
