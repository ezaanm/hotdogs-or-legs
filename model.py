import numpy as np
import os

import keras
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from keras.layers import Convolution2D, MaxPooling2D
from keras.utils import np_utils
from keras.layers import Dense, Dropout, Activation, Flatten
from keras import backend as K 


def load_train_save():

    #load in data
    x_train = "./data/train"
    x_test = "./data/test"
    epochs = 10
    batch_size = 16

    #target img dimensions, training/testing sample details
    img_width, img_height = 150, 150
    nb_train_samples = 126 
    nb_test_samples = 11

    #channel specs
    if K.image_data_format() == 'channels_first':
        input_shape = (3, img_width, img_height)
    else:
        input_shape = (img_width, img_height, 3)

    #train the model
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

    #compile the model
    model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
    
    #used an ImageDataGenerator to prevent overfitting and improve generalization,
    #as the number of images for training was pretty small
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

    #save the model for flask app to ref
    model.save("hd_or_legs.h5")

    return model

load_train_save()