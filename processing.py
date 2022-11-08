from nltk.tokenize import word_tokenize 
from nltk.stem import PorterStemmer 
from nltk.corpus import stopwords 
import string 
import numpy as np 


def process(sentence):
    """
    Pre-process a text for ML tasks 
    - Remove punctuations 
    - Tokenize
    - Remove stop words 
    - Stem each word   
    """
    sw = stopwords.words('english')
    stemmer = PorterStemmer()
    processed_tokens = []
    ignore = ['’']
    ignore.extend(string.punctuation)

    punctless = ""
    
    for char in sentence:
        if char not in ignore:
            punctless += char 

    tokens = word_tokenize(punctless)      
    for term in tokens:
        # if term not in sw :
        processed_tokens.append(stemmer.stem(term))

    return processed_tokens        

# EXAMPLE 
# check = "Greetings, thanks for visiting. How may i help you?"
# print(check + "\n") 
# print(word_tokenize(check))

def bow(tokens, corpus):
    """
    Create text vectorization using BAG OF WORDS model
    """

    # processed_sentence = [stemmer.stem(term) for term in tokens if term not in ignore]
    init_bag = np.zeros(len(corpus), dtype = np.float32)

    for i, term in enumerate(corpus):
        if term in tokens:
            init_bag[i] = 1.0
    return init_bag     


# EXAMPLE 
# print(bow(['greet', 'thank', 'visit', 'how', 'may', 'help'], 
# ['Greetings', ',', 'thanks', 'for', 'visiting', '.', 'How', 'may', 'i', 'help', 'you', '?']))   








