import pytest 
import sys 
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import facenet
from facenet.utils import detect_face

def test_fixed_batch_process():
    print("current path: \n", os.getcwd())
    print("hello") 
    #detect_face.fixed_batch_process(None, None)
    
