import torch 
from torch import nn 
import numpy as np 
import os 

# emma_notes: passing nn.Module means PNet is a sub-class of torch module 
class PNet(nn.Module):
    """
    MTCNN PNet. 

    Keyword Arguments:
        pretrained {bool} -- Whether or not to load saved pretrained weights (default: {True})
    """

    def __init__(self, pretrained=True):
        super().__init__()

        self.conv1 = nn.Conv2d(3, 10, kernel_size=3)
        self.prelu1 = nn.PReLU(10)
        self.pool1 = nn.MaxPool2d(2, 2, ceil_mode=True)
        self.conv2 = nn.Conv2d(10, 16, kernel_size=3)
        self.prelu2 = nn.PReLU(16)
        self.conv3 = nn.Conv2d(16, 32, kernel_size=3)
        self.prelu3 = nn.PReLU(32)
        self.conv4_1 = nn.Conv2d(32, 2, kernel_size=1)
        self.softmax4_1 = nn.Softmax(dim=1)
        self.conv4_2 = nn.Conv2d(32, 4, kernel_size=1)

        self.training = False 

        if pretrained:
            # emma_notes: so the pnet.pt is the so called the trained model output data file?
            state_dict_path = os.path.join(os.path.dirname(__file__), '../data/pnet.pt')
            state_dict = torch.load(state_dict_path)
            self.load_state_dict(state_dict)

    """
    Forward pass of the model.

    Args:
        x (torch.Tensor): Input tensor or batch of tensors 
    Returns:
        torch.Tensor: Output tensor or batch of tensors. 

    Performs the forward pass of the model, applying the necessary computations to the input tensor(s).
    This method is automatically called when the model is invoked, and it defines how the input is processed
    to generate the output. You can use any desired tensor operations and other modules within this methods. 
    """
    def forward(self, x):
        x = self.conv1(x)
        x = self.prelu1(x)
        x = self.pool1(x)
        x = self.conv2(x)
        x = self.prelu2(x)
        x = self.conv3(x)
        x = self.prelu3(x)
        a = self.conv4_1(x)
        a = self.softmax4_1(a)
        b = self.conv4_2(x)
        return b, a 
    

