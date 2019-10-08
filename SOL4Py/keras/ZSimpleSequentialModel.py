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

#  ZSimpleSequentialModel.py

# encodig: utf-8
import os
import sys

import keras

from keras.models import Sequential
from keras.layers import *

# This is a very simple Keras Deep CNN sequential model derived from keras.models.Sequentail
 
# See: https://keras.io/examples/cifar10_cnn/

class ZSimpleSequentialModel(keras.models.Sequential):
  ##
  # Constructor
  def __init__(self, input_shape, n_classes):
    super(ZSimpleSequentialModel, self).__init__()

    # Create a sequential model, and add keras.layers.* to the model
    self.add(Conv2D(32, kernel_size=(3, 3),  padding = 'same', input_shape = input_shape))
    self.add(Activation('relu'))
    
    self.add(Conv2D(32, kernel_size=(3, 3), padding = 'same'))
    self.add(Activation('relu'))
    
    self.add(MaxPool2D(pool_size = (2, 2)))
    self.add(Dropout(0.25))

    self.add(Conv2D(64, kernel_size=(3, 3), padding = 'same'))
    self.add(Activation('relu'))

    self.add(Conv2D(64, kernel_size=(3, 3), padding = 'same')) 
    self.add(Activation('relu'))

    self.add(MaxPool2D(pool_size = (2, 2)))
    self.add(Dropout(0.25))

    self.add(Flatten())
    self.add(Dense(512))
    self.add(Activation('relu'))
    self.add(Dropout(0.5))
    
    self.add(Dense(n_classes))
    
    self.add(Activation('softmax'))


