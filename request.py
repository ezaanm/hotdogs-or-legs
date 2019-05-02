#send requests with the feautres to the server\

import numpy as np
import os

import keras
from keras.models import Sequential, load_model
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from keras.utils import np_utils
from keras import backend as K 

#takes in image_url and adjusts to handle the image tensorization
def load_image(img_url):
    img = load_img(img_url, target_size=(150,150))
    img_tensor = img_to_array(img)
    img_tensor = np.expand_dims(img_tensor, axis=0)
    img_tensor /= 255.
    return img_tensor

#predict function, outputs the string class
def predict_on_image(model, img_url):
    img = load_image(img_url)
    output = np.array2string(model.predict(img)[0])
    output = round(float(output.strip("[]")))
    if (output == 0) : return "hotdog"
    else : return "legs"

#passes the model in to predict_on_image
def predict(img_url):
    model = load_model('./hd_or_legs.h5')
    print(predict_on_image(model, img_url))
    return predict_on_image(model, img_url)

predict('./data/train/legs/0061.jpg')