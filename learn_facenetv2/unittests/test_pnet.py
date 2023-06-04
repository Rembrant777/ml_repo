import pytest 
import torch 
import os 
import sys
from PIL import Image 
from torchvision.transforms import ToTensor

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import facenet
from facenet.pnet import PNet

"""
In MTCNN PNet will be executed in the first stage. 
"""

def test_PNet():
    pnet = PNet(pretrained=False)

    # load image to preprocess 
    img_path = os.path.join(os.path.dirname(__file__), '../data/test_images/angelina_jolie/1.jpg')
    img = Image.open(img_path).convert('RGB')
    img_tensor = ToTensor()(img)

    # process img upon the PNet 
    output = pnet(img_tensor.unsqueeze(0))

    # output results bounding_box, landmarks 
    b_boxes, landmarks = output 

    print("Bounding boxes: ")
    print(b_boxes)
    print("Landmarks: ")
    print(landmarks)
