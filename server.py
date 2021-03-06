import os
import json
import time
import threading
from flask import Flask, render_template, request, jsonify
import numpy as np

import keras
from keras.models import Sequential, load_model
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from keras.utils import np_utils
from keras import backend as K 

from modelUtils import load_image, predict, time_and_prediction_for_images, get_accuracy
from entities import Leaderboard

app = Flask(__name__)

#create global variables
lead = Leaderboard()

fightPhotos = []
fightLabels = ["hotdogs", "hotdogs", "legs", "hotdogs", "legs", "legs", "legs", "legs"]
fightStartTime = 0
fightEndTime = 0
machineFightTime = 0
machineAccuracy = 4

#splash screen
@app.route("/")
def splash():
  return render_template("splash.html")
  
#shuffles photos and labels by same index
def shuffleFight():
  p = np.random.permutation(8)
  global fightPhotos, fightLabels
  fightPhotos = np.array(fightPhotos)
  fightLabels = np.array(fightLabels)
  fightPhotos = fightPhotos[p]
  fightLabels = fightLabels[p]
  
#begin the classifiers run on the fight photos
def machineFight():
  global machineFightTime, machineAccuracy
  tf, predictions = time_and_prediction_for_images(fightPhotos)
  accuracy = get_accuracy(predictions, fightLabels)
  machineAccuracy = accuracy * len(fightLabels)
  machineFightTime = tf
  
machineFightThread = threading.Thread(target=machineFight)
    
#start of fight screen
@app.route("/fight", methods=["GET"])
def fight():
  shuffleFight()
  return render_template("fight.html")
  
#update the leaderboard
@app.route("/leaderboard", methods=["POST"])
def leaderboard():
  global lead
  name = request.form.get('name')
  time = float(request.form.get('time'))
  lead.put(name, time)
  return render_template("splash.html")
  
#move next image and update scores in the fight
@app.route("/fightPlay", methods=["POST"])
def fightPlay():
  global fightStartTime, fightEndTime, machineFightThread
  index = int(request.form.get('index'))
  correct = int(request.form.get('correct'))
  response = request.form.get('response')
  if index > 0 and response == fightLabels[index - 1]: 
    correct += 1
  elif index == 0:
    fightStartTime = time.time()
    machineFightThread = threading.Thread(target=machineFight)
    machineFightThread.start()
    
  if index == 8:
    fightEndTime = time.time()
    elapsedTime = fightEndTime - fightStartTime
    while (machineFightThread.is_alive()):
      time.sleep(1)
    
    machineFightThread.join()
    return render_template("fightSummary.html", score=correct, time=elapsedTime, maAcc = machineAccuracy, maTime = machineFightTime, leaderboard=lead)
  
  return render_template("fightStart.html", nextIndex=index+1, imageLink=fightPhotos[index], score=correct)

#go to the test page
@app.route("/test", methods=["GET"])
def test():
  return render_template("test.html")
  
#upload a photo
@app.route("/testUpload", methods=["POST"])
def test_upload():
  file = request.files['image']
  filename = os.path.join("static/uploads/", file.filename)
  file.save(filename)
  classification = predict(filename)
#  os.remove(filename) - we are going to learn about your dog preferences and target u with ads!
  
  return render_template("test.html", imageLink = filename, classification = classification)

if __name__ == "__main__":
  fightPhotos = [os.path.join("static/fight/", f) for f in os.listdir("static/fight/") if os.path.isfile(os.path.join("static/fight/", f))]
  
  if (os.path.isfile(os.path.join("static/fight/", ".DS_Store"))):
    fightPhotos.remove("static/fight/.DS_Store")
    
  fightPhotos.sort()
  app.run(port=5000, debug=True)