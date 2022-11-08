import json 
import torch 
from model import Net
from processing import process, bow
import random 
import streamlit as st 
from streamlit_chat import message
import time
import random 

# LOADING INTENTS AND MODEL
intents = json.loads(open('intents.json').read())
FILE = "data.pth"
data = torch.load(FILE)
model_state = data['model_state']
input_size = data['input_size']
hidden_size = data['hidden_size']
output_size = data['output_size']
corpus = data['corpus']
labels = data['labels']
model = Net(input_size, hidden_size, output_size)
model.load_state_dict(model_state)
model.eval()


# APP
placeholder = st.empty()
sentence = st.text_input('', key = "input")

if 'history' not in st.session_state:
    st.session_state['history'] = []

with placeholder.container():
    message('hello') 
    if sentence:  
        sentence_processed = process(sentence)
        X = bow(sentence_processed, corpus)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X)

        #INFERENCE
        output = model(X)    
        _, predicted = torch.max(output, dim = 1)
        label = labels[predicted.item()]

        proba = torch.softmax(output, dim = 1)
        prob = proba[0][predicted.item()]
            
        if prob.item() > 0.75:
            for intent in intents['intents']:
                if label == intent['label']:
                    response = (random.choice(intent['response']))
                    

        else:
            response = "Oops, I don't understand that"
        
        # message(sentence, is_user = True)
        # # time.sleep(2)
        # message(label)
        # message(prob.item())
        # message(response)
        
        user_message = {
            "message": sentence,
            "is_user": True
            }
        bot_message =  {
            "message": response,
            "is_user": False
            }        
        st.session_state.history.append(user_message)
        st.session_state.history.append(bot_message)

        keys = random.sample(range(1000, 9999), len(st.session_state.history))

        for i, chat in enumerate(st.session_state.history):
            message(**chat, key = keys[i])








