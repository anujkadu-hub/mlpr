nltk.download('treebank') 
nltk.download('universal_tagset') 
 
nltk_data = list(nltk.corpus.treebank.tagged_sents(tagset='universal')) 
print(nltk_data[:2])
for sent in nltk_data[:2]: 
  for w in sent: 
    print(w)
