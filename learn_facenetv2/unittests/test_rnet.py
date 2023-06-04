import pytest 
import torch 
import os 
import sys 
from PIL import Image 
from torchvision.transforms import ToTensor

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import facenet
from facenet.pnet import PNet
from facenet.rnet import RNet

"""
In MTCNN RNet will be execute in the second stage. 
RNet's input entity is the output of the PNet's output entity. 
"""

def test_RNet():
    input_data = torch.randn(1, 3, 48, 48)
    rnet = RNet(pretrained=False)
    
    # set model mode to eval 
    rnet.eval()

    output = rnet(input_data)

    print("Output shape: ", output[0].shape, output[1].shape)



