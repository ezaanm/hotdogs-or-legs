import os
import json
import time
from flask import Flask, render_template, request, jsonify
import numpy as np

import keras
from keras.models import Sequential, load_model
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from keras.utils import np_utils
from keras import backend as K 

app = Flask(__name__)

fightPhotos = []
fightLabels = ["hotdogs", "hotdogs", "hotdogs", "hotdogs", "legs", "legs", "legs", "legs"]
startTime = 0
endTime = 0

@app.route("/")
def splash():
  return render_template("splash.html")

def shuffleFight():
  p = np.random.permutation(8)
  global fightPhotos
  global fightLabels
  fightPhotos = np.array(fightPhotos)
  fightLabels = np.array(fightLabels)
  fightPhotos = fightPhotos[p]
  fightLabels = fightLabels[p]
  
@app.route("/fight", methods=["GET"])
def fight():
  shuffleFight()
  return render_template("fight.html")
  
@app.route("/fightPlay", methods=["POST"])
def fightPlay():
  index = int(request.form.get('index'))
  correct = int(request.form.get('correct'))
  response = request.form.get('response')
  if index > 0 and response == fightLabels[index - 1]: 
    correct += 1;
  elif index == 0:
    global startTime
    startTime = time.time()
    
  if index == 8:
    global endTime
    endTime = time.time()
    elapsedTime = endTime - startTime
    return render_template("fightSummary.html", score=correct, time=elapsedTime)
  
  return render_template("fightStart.html", nextIndex=index+1, imageLink=fightPhotos[index], score=correct)

@app.route("/test", methods=["GET"])
def test():
  return render_template("test.html")
  
@app.route("/test_upload", methods=["POST"])
def test_upload():
  file = request.files['image']
  filename = os.path.join("static/uploads/", file.filename)
  file.save(filename)
  
  classification = predict(filename)

#  os.remove(filename) - we are going to learn about your dog preferences and target u with ads!
  
  return render_template("test.html", imageLink = filename, classification = classification)

  #call predict with the image route from wherever u need to get the response
  #"hotdogs" or "legs"

def load_image(img_url):
    img = load_img(img_url, target_size=(150,150))
    img_tensor = img_to_array(img)
    img_tensor = np.expand_dims(img_tensor, axis=0)
    img_tensor /= 255.
    return img_tensor

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
    predictions += predict(img)
  tf = time.time() - t0
  return [tf, predictions]

def get_accuracy(pred, actual):
  pred_ = np.array(pred)
  actual_ = np.array(actual)
  accuracy = (np.sum(pred_ == actual_))/len(pred_)
  return accuracy
  
#  once classified, delete image

if __name__ == "__main__":
  fightPhotos = [os.path.join("static/fight/", f) for f in os.listdir("static/fight/") if os.path.isfile(os.path.join("static/fight/", f))]
  fightPhotos.remove("static/fight/.DS_Store")
  fightPhotos.sort()
  app.run(port=5000, debug=True)