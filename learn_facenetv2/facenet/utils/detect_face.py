import torch
from torch.nn.functional import interpolate 
from torchvision.transforms import functional as F 
from torchvision.ops.boxes import batched_nms 
from PIL import Image
import numpy as np
import os 
import math 

## define macro variables 
BATCH_SIZE = 512

# OpenCV is optinal, but required if using numpy arrays instead of PIL 
try:
    import cv2 
except:
    pass 

def fixed_batch_process(im_data, model):
    print("fixed_batch_process called!")
    # out = []
    # for i in range(0, len(im_data), BATCH_SIZE):
    #     batch = im_data[i:(i+BATCH_SIZE)]
    #     out.append(model(batch))

    # return tuple(torch.cat(v, dim=0) for v in zip(*out))