from nltk.tokenize import word_tokenize 
from nltk.stem import PorterStemmer 
from nltk.corpus import stopwords 
from typing import List
import numpy as np 
import string 


def process(sentence: str) -> List[str]:
    """
    Pre-process a text for NLP tasks.
    - Remove punctuations
    - Tokenize
    - Remove stop words
    - Stem each word

    Args:
        sentence (str): The input text to be pre-processed.

    Returns:
        list: A list of pre-processed and stemmed tokens.

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

def bow(
        tokens: List[str],
        corpus: List[str]
) -> np.ndarray:
    """
    Create text vectorization using the Bag of Words (BoW) model.

    Args:
        tokens (list): List of pre-processed and stemmed tokens.
        corpus (list): List of terms in the corpus.

    Returns:
        numpy.ndarray: A BoW vector representing the input tokens.

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








