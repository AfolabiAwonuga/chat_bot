import json 
import torch
import numpy as np
import torch.nn as nn 
from model import Net
from processing import bow
from processing import process
from nltk.tokenize import word_tokenize 
from torch.utils.data import Dataset, DataLoader 


intents = json.loads(open('intents.json').read())


# PRE-PROCESSING INTENT PATTERNS
corpus = []
labels = []
data = []

for intent in intents['intents']:
    labels.append(intent['label'])
    for pattern in intent['pattern']:
        corpus.extend(process(pattern))
        data.append((process(pattern), intent['label']))


corpus = sorted(set(corpus))
labels = sorted(labels)
# print(terms)
# print('\n')
# print(labels)
# print('\n')
# print(index)

# BAG OF WORDS (vectorization of processed patterns)
X = []
y = []
for (feat, target) in data:
    X.append(bow(feat, corpus))
    y.append(labels.index(target))

X = np.array(X)
y = np.array(y)

# print(len(X[0]), len(corpus))
# print('\n')
# print(y, len(y))

# TORCH SET (custom pytorch dataset)
class TrainSet(Dataset):
    """
    Custom dataset class for training data.

    This class represents a dataset with input features (X) and corresponding
    target labels (y).

    Attributes:
        X (list): List of input samples (features).
        y (list): List of target labels.

    """
    def __init__(self):
        """
        Initialize the dataset.

        Args:
            X (list): List of input samples (features).
            y (list): List of target labels.

        """
        self.n_samples = len(X)
        self.x = X
        self.y = y

    def __getitem__(self, index: int)-> tuple:
        """
        Get a specific item from the dataset.

        Args:
            index (int): Index of the item to retrieve.

        Returns:
            tuple: A tuple containing the input feature and target label.

        """
        return self.x[index], self.y[index]

    def __len__(self) -> int:
        """
        Get the total number of samples in the dataset.

        Returns:
            int: Total number of samples.

        """
        return self.n_samples


train_set = TrainSet()
loader = DataLoader(dataset = train_set, batch_size = 8, shuffle = True, num_workers = 0)                

input_size = len(X[0])
hidden_size = 8
output_size = len(labels)

# print(input_size)

# TRAINING BOT 
model = Net(input_size, hidden_size, output_size)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr = 0.001)

epochs = 1000
for epoch in range(epochs):
    for (feat, target) in loader:
        outputs = model(feat)
        loss = criterion(outputs, target) 
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    if (epoch + 1) % 100 == 0:
        print(f"epoch {epoch+1}/{epochs}, loss={loss.item():.4f}")

print(f"final loss, loss={loss.item():.4f}")        

# SAVING MODEL
data = {
    "model_state": model.state_dict(),
    "input_size": input_size,
    "output_size": output_size,
    "hidden_size": hidden_size,
    "corpus": corpus,
    "labels": labels
}

FILE = "data.pth"
torch.save(data, FILE)