! pip install spacy
! pip install nltk 
import spacy 
 
nlp=spacy.load("en_core_web_sm") 
 
MyText = "sita is cute and smart. sita likes dogs and cats." 
MyDoc = nlp(MyText) 
type(MyDoc) 
spacy.tokens.doc.Doc 
 
for token in MyDoc: 
  print(token.text)

for sent in MyDoc.sents: 
  print(sent)

import nltk 
nltk.download('punkt_tab') 
MyText = "sita is cute and smart. she likes cats and dogs. i AM FINDING JOB." 
from nltk.tokenize import sent_tokenize, word_tokenize 
sent_tokenize(MyText)
