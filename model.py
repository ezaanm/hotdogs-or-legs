# develop and train the model

import numpy as np
import os

import keras
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from keras.layers import Convolution2D, MaxPooling2D
from keras.utils import np_utils
from keras.layers import Dense, Dropout, Activation, Flatten
from keras import backend as K 

#https://gist.github.com/fchollet/0830affa1f7f19fd47b06d4cf89ed44d
#from data import
def load_and_train_model():
    x_train = "./data/train"
    x_test = "./data/test"
    epochs = 10
    batch_size = 16

    img_width, img_height = 150, 150
    nb_train_samples = 114 
    nb_test_samples = 4


    if K.image_data_format() == 'channels_first':
        input_shape = (3, img_width, img_height)
    else:
        input_shape = (img_width, img_height, 3)


    model = Sequential()
    model.add(Convolution2D(32, (3,3), input_shape=input_shape))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))

    model.add(Convolution2D(32,(3,3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))

    model.add(Convolution2D(64,(3,3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))

    model.add(Flatten())
    model.add(Dense(64))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(1))
    model.add(Activation('sigmoid'))

    model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
    
    train_datagen = ImageDataGenerator(
        rescale=1. / 255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True
    )
    
    test_datagen = ImageDataGenerator(rescale=1. / 255)

    train_generator = train_datagen.flow_from_directory(
        x_train,
        target_size=(img_width, img_height),
        batch_size=batch_size,
        class_mode='binary'
    )
    
    test_generator = test_datagen.flow_from_directory(
        x_test,
        target_size=(img_width, img_height),
        batch_size=batch_size,
        class_mode='binary'
    )

    model.fit_generator(
        train_generator,
        steps_per_epoch=nb_train_samples // batch_size,
        epochs=epochs,
        validation_data=test_generator,
        validation_steps = nb_test_samples // batch_size
    )

    # model.fit(x_train)

    return 


load_and_train_model()