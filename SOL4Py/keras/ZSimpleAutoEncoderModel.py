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
 
# 2019/05/10

# ZSimpleAutoEncoderModel.py

# encodig: utf-8

# This class is based on https://blog.keras.io/building-autoencoders-in-keras.html


from keras.layers import Input, Dense, Conv2D, MaxPooling2D, UpSampling2D
from keras.models import Model
from keras import backend as K

class ZSimpleAutoEncoderModel(Model):

  def __init__(self, input_shape):
    self.input_image  = Input(shape=input_shape)
    self.decoded = self.build(self.input_image)
    Model.__init__(self, self.input_image, self.decoded)


  def build(self, input_image):
    encoded = self.encode(input_image)
    decoded = self.decode(encoded)
    return decoded 
 
  # This is an encode method for MNIST
  # If required, please redefine your own encode method in a subclass derived from this class.
  def encode(self, input_image):
    x = Conv2D(16, (3, 3), activation='relu', padding='same')(input_image)
    x = MaxPooling2D((2, 2),                  padding='same')(x)
    x = Conv2D( 8, (3, 3), activation='relu', padding='same')(x)
    x = MaxPooling2D((2, 2),                  padding='same')(x)
    x = Conv2D( 8, (3, 3), activation='relu', padding='same')(x)
    encoded = MaxPooling2D((2, 2),            padding='same')(x)
    return encoded

  # This is a deocoder or MNIST
  # If required, please redefine your own decode method in a subclass derived from this class.
  def decode(self, encoded):
    x = Conv2D( 8, (3, 3), activation='relu',         padding='same')(encoded)
    x = UpSampling2D((2, 2))(x)
    x = Conv2D( 8, (3, 3), activation='relu',         padding='same')(x)
    x = UpSampling2D((2, 2))(x)
    x = Conv2D(16, (3, 3), activation='relu'                        )(x)
    x = UpSampling2D((2, 2))(x)
    decoded = Conv2D(1, (3, 3), activation='sigmoid', padding='same')(x)
    
    return decoded

 

