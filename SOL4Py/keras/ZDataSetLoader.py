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

# 2019/04/24 

#  ZDataSetLoader.py

# encodig: utf-8
import os
import sys
import glob
import numpy as np
import traceback
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from keras.preprocessing.image import load_img, img_to_array
from keras.utils import np_utils
from PIL import Image

class ZDataSetLoader:
  ##
  # Constructor
  def __init__(self, test_size=0.2):
    self.x_train = None #
    self.x_test  = None #
    self.y_train = None #
    self.y_test  = None #

    self.test_size = test_size


  # dataset parameter takes a tubple like ("./dataset_folder", "png")
  
  def load_dataset(self, dataset, image_size=128):
    self.dataset_folder, self.load_format = dataset
    self.CHANNELS    = 3
    self.image_size  = image_size

    x = []  # a list of images which read from image files under self.data_folder.
    y = []  # a list of one_host labels corresponding to each image in the image list x.
    
    # We assume that subfolders under the self.dataset_folder are class-names of the image list x.
    # self.classes are a set of class names which can be recognized by human.

    if os.path.exists(self.dataset_folder) == False:
      print("Not found folder {}".format(self.dataset_folder))
      return
      
    self.classes = sorted( os.listdir(self.dataset_folder) )
    print(self.classes)
    self.n_classes = len(self.classes)
    
    for index, folder in enumerate(self.classes):
      dir = os.path.join(self.dataset_folder, folder)
      print("Reading image files in folder: " + dir)

      files = glob.glob(dir + "/*." + self.load_format)
      for _, file in enumerate(files):
        try:
          # Load an image from the file by using keras load_img
          image = load_img(file, target_size=(image_size, image_size))
          array = img_to_array(image)
          #array = array.reshape(self.image_size, self.image_size, 3)

          # Convert a value range of the array to be within range[0, 1.0]
          #array = array.astype('float32')/255.0
          x.append(array)
          y.append(index)

        except:
          traceback.print_exc()
     
    x = np.array(x)
    y = np.array(y)
    
    # Convert y to onehot expressions. 
    #y = np_utils.to_categorical(y, len(self.classes))

    # Split data x and label y to train and test by using train_test_split.
    #x_train: train_data
    #x_test : test_data
    #y_train: onehot labels for x_train
    #y_test : onehot labels for x_test
    self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(x, y,  test_size=self.test_size)

    # Convert x to be within range[0, 1.0]
    self.x_train = self.x_train.astype('float32')/255.0
    self.x_test  = self.x_test. astype('float32')/255.0
    
    # Convert y to onehot vector. 
    self.y_train = np_utils.to_categorical(self.y_train, self.n_classes)
    self.y_test  = np_utils.to_categorical(self.y_test,  self.n_classes)

    #flattened_image_size = self.image_size * self.image_size * self.CHANNELS 
    #self.x_train = self.x_train.reshape(self.x_train.shape[0], flattened_image_size)
    #self.x_test  = self.x_test. reshape(self.x_test.shape[0],  flattened_image_size)


  def show_summary(self, show_images=True, show_labels=True):
    print("x_train: len:" + str(len(self.x_train)) )
    print(self.x_train)
    print("x_test : len:" + str(len(self.x_test)) )
    print(self.x_test)
    
    print("y_train: len:" + str(len(self.y_train)) )
    print(self.y_train)
    print("y_test : len:" + str(len(self.y_test)) )
    print(self.y_test)
    if (show_images==True):
      self.show_sampling_images(6, 6, show_labels)


  # Show sampling images and class names taken from top row*col of self.trains and self.y_trains. 
  def show_sampling_images(self, row, col, show_labels):
    plt.subplots_adjust(wspace=0.4, hspace=0.8)

    for i in range(col*row):
      try:
        image = self.x_train[i].reshape(self.image_size, self.image_size, self.CHANNELS)
        plt.subplot(row, col, i+1)

        plt.imshow(image, interpolation='nearest', 
                 extent=(0, self.image_size, 0, self.image_size) )

        name = self.get_class_name(self.y_train[i])
        plt.axis('off')  
        if show_labels==True:
          plt.title(name)
      except:
        pass
        
    plt.show()


  def get_class_name(self, onehot):
    name = ""
    for i in range(len(onehot)):
      if onehot[i] == 1:
        name = self.classes[i]
        break
        
    return name

