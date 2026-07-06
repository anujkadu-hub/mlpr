import nltk 
from nltk import ne_chunk 
nltk.download('punkt_tab') 
nltk.download('averaged_perceptron_tagger_eng') 
! pip install svgling 
 
new = "The big cat ate the little mouse who was after fresh cheese" 
nt = nltk.pos_tag(nltk.word_tokenize(new)) 
grammer_np = r"NP: {<DT>?<JJ>*<NN>}" 
chunk_parser = nltk.RegexpParser(grammer_np) 
chunk_result = chunk_parser.parse(nt) 
chunk_result
