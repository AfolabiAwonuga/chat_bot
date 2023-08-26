import torch 
import torch.nn as nn 
from torch.utils.data import Dataset, DataLoader 


class Net(nn.Module):
    """
    A simple feedforward neural network class.

    This class defines a feedforward neural network with specified input size,
    hidden size, and number of classes.

    Attributes:
        input_size (int): The size of the input features.
        hidden_size (int): The size of the hidden layer.
        num_classes (int): The number of output classes.

    """
    def __init__(
            self, 
            input_size: int, 
            hidden_size: int, 
            num_classes: int
    ):
        """
        Initialize the neural network.

        Args:
            input_size (int): The size of the input features.
            hidden_size (int): The size of the hidden layer.
            num_classes (int): The number of output classes.

        """
        super(Net, self).__init__()
        self.l1 = nn.Linear(input_size, hidden_size)
        self.l2 = nn.Linear(hidden_size, hidden_size)
        self.l3 = nn.Linear(hidden_size, num_classes)
        self.relu = nn.ReLU()


    def forward(
            self, 
            x: torch.Tensor
    ) -> torch.Tensor:
        """
        Forward pass of the neural network.

        Args:
            x (torch.Tensor): Input tensor.

        Returns:
            torch.Tensor: Output tensor.

        """
        out = self.l1(x) 
        out = self.relu(out) 
        out = self.l2(out)
        out = self.relu(out) 
        out = self.l3(out) 
        return out 
