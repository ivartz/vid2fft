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

# 2019/04/30 

#  ZSuperResolutionSequentialModel.py
# See: https://arxiv.org/pdf/1501.00092.pdf
#      https://software.intel.com/en-us/articles/an-example-of-a-convolutional-neural-network-for-image-super-resolution

# encodig: utf-8
import os
import sys

import keras

from keras.models import Sequential
from keras.layers import *


class ZSuperResolutionSequentialModel(keras.models.Sequential):
  ##
  # Constructor
  def __init__(self, input_shape):
    super(ZSuperResolutionSequentialModel, self).__init__()

    # Create a sequential model, and add keras.layers.* to the model
    self.add(Conv2D(filters=64, kernel_size=(9, 9), padding = 'same', input_shape = input_shape))
    self.add(Activation('relu'))
    
    self.add(Conv2D(filer=32,  kernel_size=(1, 1),  padding = 'same'))
    self.add(Activation('relu'))

    self.add(Conv2D(filter=3,  kernel_size=(5, 5),  padding = 'same'))
    self.add(Activation('relu'))


  
