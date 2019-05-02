import os
import json
import time
import numpy as np
import keras
from keras.models import Sequential, load_model
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from keras.utils import np_utils
from keras import backend as K 
  
def load_image(img_url):
    img = load_img(img_url, target_size=(150,150))
    img_tensor = img_to_array(img)
    img_tensor = np.expand_dims(img_tensor, axis=0)
    img_tensor /= 255.
    return img_tensor

#call predict with the image route from wherever u need to get the response
#"hotdogs" or "legs"
def predict(img_url):
    model = load_model('./hd_or_legs.h5')
    img = load_image(img_url)
    output = np.array2string(model.predict(img)[0])
    output = round(float(output.strip("[]")))
    if (output == 0) : return "hotdogs"
    else : return "legs"

#returns time and predictions in a list
def time_and_prediction_for_images(images):
  t0 = time.time()
  predictions = []
  for img in images:
    predictions.append(predict(img))
  tf = time.time() - t0
  return tf, predictions

def get_accuracy(pred, actual):
  pred_ = np.array(pred)
  actual_ = np.array(actual)
  accuracy = (np.sum(pred_ == actual_))/len(pred_)
  return accuracy