import nltk 
from nltk.chat.util import Chat, reflections 
pairs=[ 
    [ 
        r"My name is (.*)", 
        ["Hello %1, How are you today?",] 
    ], 
    [ 
        r"hi|hey|hello", 
        ["Hello","Hey there",] 
    ], 
    [ 
        r"What is your name?", 
        ["My name is Chatbot",] 
    ], 
    [ 
        r"How are you?", 
        ["I'm doing good. How about you?",] 
    ], 
    [ 
        r"Sorry (.*)", 
        ["Its alright", "It's ok, Never mind",]
       ], 
    [ 
        r"I'm (.*) doing good", 
        ["Nice to hear that", "How can I help you?",] 
    ], 
    [ 
        r"(bye|goodbye|exit|quit)", 
        ["Goodbye! Have a nice day.", "See you later!"] 
    ], 
] 
 
def chat(): 
  print("Hi, I am a chatbot created for NLP Practical") 
  chat=Chat(pairs, reflections) 
  chat.converse() 
 
if __name__ == "__main__": 
  chat()
