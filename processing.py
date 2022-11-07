from nltk.tokenize import word_tokenize 
from nltk.stem import PorterStemmer 
from nltk.corpus import stopwords 
import string 
import numpy as np 

def process(sentence):
    sw = stopwords.words('english')
    stemmer = PorterStemmer()
    processed_tokens = []
    ignore = ['’']
    ignore.extend(string.punctuation)
    puntless = ""
    
    for char in sentence:
        if char not in ignore:
            puntless += char 

    tokens = word_tokenize(puntless)      
    for term in tokens:
        if term not in sw :
            processed_tokens.append(stemmer.stem(term))

    return processed_tokens        
# check = "Greetings, thanks for visiting. How may i help you?"

# print(check + "\n") 
# print(process(check))

def bow(processed_sentence, corpus):
    init_bag = np.zeros(len(corpus), dtype =np.float32)
    for i, term in enumerate(corpus):
        if term in processed_sentence:
            init_bag[i] = 1.0
    return init_bag     


# print(bow(['greet', 'thank', 'visit', 'how', 'may', 'help'], 
# ['afternoon', 'are', 'avail', 'boss', 'built', 'bye', 'cancel', 
# 'charg', 'day', 'deliv', 'even', 'good', 'goodby', 'greet', 'hello', 
# 'hey', 'hi', 'how', 'human', 'i', 'im', 'look', 'made', 'method', 'morn', 
# 'name', 'order', 'pay', 'payment', 'perfum', 'purchas', 'question', 'revers',
#  'robot', 'stoke', 'tell', 'thank', 'use', 'way', 'what', 'whi', 'who', 'yoou']))   








