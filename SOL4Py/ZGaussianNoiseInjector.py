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
 
#  ZGaussianNoiseInjector.py

# encoding: utf-8

import sys
import os
import numpy as np

import traceback

from SOL4Py.ZNoiseInjector import *

class ZGaussianNoiseInjector(ZNoiseInjector):
  ##
  # Constructor
  def __init__(self, sigma=40):
    self.sigma = sigma

  def inject_to(self, image):
    src_image = image.astype(np.float32)
    # 1 Create a zero-filled image from the src_image. 
    noised_image = np.zeros(image.shape, np.float32)

    # 2 Create a one channel noise.
    noise = np.random.randn(image.shape[0], image.shape[1]) * self.sigma
    noise = noise.astype(np.float32)

    # 3 Add the noise to the source image.
    if len(noised_image.shape) == 2: # Grayscale 
      noised_image = image + noise
    else:
      noised_image[:,:, 0] = image[:,:, 0] + noise
      noised_image[:,:, 1] = image[:,:, 1] + noise
      noised_image[:,:, 2] = image[:,:, 2] + noise

    noised_image = np.clip(noised_image, 0.0, 255.0)
    noised_image = noised_image.astype(np.uint8)

    return noised_image

