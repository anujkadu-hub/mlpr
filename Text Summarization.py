!pip install sumy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

text = "AI encompasses a broad range of techniques and technologies, including machine learning and deep learning. Machine learning involves creating models by training algorithms to make predictions or decisions based on data. It includes various techniques such as linear regression, decision trees, and neural networks. Deep learning, a subset of machine learning, uses multilayered neural networks to simulate the decision-making power of the human brain."

doc = PlaintextParser.from_string(text, Tokenizer("english"))
summary = LsaSummarizer()(doc.document, 2)

for s in summary:
    print(s)
