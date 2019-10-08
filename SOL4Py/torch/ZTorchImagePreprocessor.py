#/******************************************************************************
# 
#  Copyright (c) 2019 Antillia.com TOSHIYUKI ARAI. ALL RIGHTS RESERVED.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#******************************************************************************/
 
# 2019/07/10

# ZTorchImagePreprocessor.py

# encodig: utf-8

import sys
import os
import time
import traceback
import numpy as np

import torch
import torchvision
import torchvision.transforms as transforms
from torch.autograd import Variable


class ZTorchImagePreprocessor:
  def __init__(self):
    pass

  def preprocess(self, image, resize=256, crop=224):
    normalize = transforms.Normalize(
                  mean=[0.485, 0.456, 0.406],
                  std =[0.229, 0.224, 0.225])

    preprocessor = transforms.Compose([
                 transforms.Resize(resize),
                 transforms.CenterCrop(crop),
                 transforms.ToTensor(),
                 normalize
                 ])
    return preprocessor(image)


  def image_crop(self, image, resize=256, crop=224):
    crop_preprocessor = transforms.Compose([
       transforms.Resize(resize),
       transforms.CenterCrop(crop)
    ])
    return crop_preprocessor(image)

