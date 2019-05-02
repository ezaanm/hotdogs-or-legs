import os
import json
from flask import Flask, render_template, request, jsonify
import numpy as np

import keras
from keras.models import Sequential, load_model
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from keras.utils import np_utils
from keras import backend as K 

app = Flask(__name__)

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def splash():
  return render_template("splash.html")
  
@app.route("/fight", methods=["GET"])
def fight():
  return render_template("fight.html")
  
@app.route("/fightPlay", methods=["POST"])
def fightPlay():
  index = request.form.get('index')
  correct = request.form.get('correct')
  return render_template("fightStart.html")
#  return render_template("fight.html", imageIndex=xxx, imageLink=, correct=)

@app.route("/test", methods=["GET"])
def test():
  return render_template("test.html")
  
@app.route("/test_upload", methods=["POST"])
def test_upload():
  file = request.files['image']
  filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
  
  file.save(f)
  
#  do some ML on the file and get classification
  
  classification = "100p a hot dog"
  os.remove(filename)
  
  return render_template("test.html", classification = classification)

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
  app.run(port=5000, debug=True)