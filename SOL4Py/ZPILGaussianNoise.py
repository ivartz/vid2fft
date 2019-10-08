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
 
# 2019/07/23

#  ZPILGaussianNoise.py

# encodig: utf-8

import sys
import os
import time
import traceback
import random
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageOps, ImageFilter

import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

from SOL4Py.ZGaussianNoiseInjector import *


# This class may be use a component of torch image transformer.
#
# transforms.Compose([ ZGaussianNoise(40),
#                       transforms.ToTensor()])

class ZPILGaussianNoise(object):
  def __init__(self, sigma):
    # Create an object ZGaussianNoiseInjector
    self.noise_injector = ZGaussianNoiseInjector(sigma=sigma)

  def __call__(self, image):
    arrayed_image = np.asarray(image)
    noised_image = self.noise_injector.inject_to(arrayed_image)

    # Create a PIL image from the noised_image
    return Image.fromarray(noised_image)

