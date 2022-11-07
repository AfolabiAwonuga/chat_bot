import json 
import torch 
from model import Net
from processing import process, bow
import random 


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


while True:
    sentence = input()
    if sentence == 'bye':
        break

    sentence = process(sentence)
    X = bow(sentence, corpus)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X)

    output = model(X)    
    _, predicted = torch.max(output, dim = 1)
    label = labels[predicted.item()]

    proba = torch.softmax(output, dim = 1)
    prob = proba[0][predicted.item()]


    if prob.item() >  0.75:
        for intent in intents['intents']:
            if label == intent['label']:
                print(f"{random.choice(intent['response'])}")

    else:
        print("i don't understand")    






