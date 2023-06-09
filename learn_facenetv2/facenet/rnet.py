import torch 
from torch import nn 
import numpy as np 
import os 
import sys 

class RNet(nn.Module):
    """
    MTCNN RNet. 

    Keyword Arguments: 
        pretrained {bool} -- Whether or not to load saved pretrained weights (default: {True})
    """

    def __init__(self, pretrained = True):
        super().__init__()

        self.conv1 = nn.Conv2d(3, 28, kernel_size=3)
        self.prelu1 = nn.PReLU(28)
        self.pool1 = nn.MaxPool2d(3, 2, ceil_mode=True)
        self.conv2 = nn.Conv2d(28, 48, kernel_size=3)
        self.prelu2 = nn.PReLU(48)
        self.pool2 = nn.MaxPool2d(48, 64, ceil_mode=True)
        self.conv3 = nn.Conv2d(48, 64, kernel_size=2)
        self.prelu3 = nn.PReLU(64)
        self.dense4 = nn.Linear(576, 128)
        self.prelu4 = nn.PReLU(128)
        self.dense5_1 = nn.Linear(128, 2)
        self.softmax5_1 = nn.Softmax(dim=1)
        self.dense5_2 = nn.Linear(128, 4)

        self.training = False 

        if pretrained:
            # emma_notes: model of RNet already trained load from disk to memory directly
            state_dict_path = os.path.join(os.path.dirname(__file__), '../data/rnet.pt')
            state_dict = torch.load(state_dict_path)
            self.load_state_dict(state_dict)


    """
    Forward pass of the model.

    Args: 
       x (torch.Tensor): Input tensor or batch of tensors
    Returns: 
       troch.Tensor: Output tensor or batch of tensors.

    Performs the forward pass of the model, applying the necessary computations to the input tensor(s).
    This method is automatically called when the model is invoked, and it defines how the input is processed
    to generate the output. You can use any desired tensor operaitons and other modules within this methods. 
    """        
    def forward(self, x):
        x = self.conv1(x)
        x = self.prelu1(x)
        x = self.pool1(x)
        x = self.conv2(x)
        x = self.prelu2(x)
        x = self.pool2(x)
        x = self.conv3(x)
        x = self.prelu3(x)
        x = x.permute(0, 3, 2, 1).contiguous()
        x = self.dense4(x.view(x.shape[0], -1))
        x = self.prelu4(x)
        a = self.dense5_1(x)
        a = self.softmax5_1(a)
        b = self.dense5_2(x)
        return b, a 