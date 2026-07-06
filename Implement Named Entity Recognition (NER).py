import nltk 
nltk.download('averaged_perceptron_tagger') 
nltk.download('maxent_ne_chunker_tab') 
nltk.download('words') 
from nltk import ne_chunk 
 
m = "The US Presedent stays in white house" 
nt=nltk.word_tokenize(m) 
ntg=nltk.pos_tag(nt) 
nr=ne_chunk(ntg) 
 
print(nr)

! second code
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp(input("Enter Text: "))

for ent in doc.ents:
    print(ent.text, ":", ent.label_)
