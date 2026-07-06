import spacy 
nlp = spacy.load("en_core_web_sm") 
 
text = "Reliance Retail acquires majority stake in designer brand Abraham & Thakore." 
doc = nlp(text) 
for token in doc: 
  print(token.text,'=>',token.dep_) 
from spacy import displacy 
displacy.render(doc, jupyter=True)
