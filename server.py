import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def splash():
  return render_template("splash.html")
  
@app.route("/fight", methods=["GET"])
def fight():
  return render_template("fight.html")

@app.route("/test", methods=["GET"])
def test():
  return render_template("test.html")
  
@app.route("/test_upload", methods=["POST"])
def test_upload():
  file = request.files['image']
  f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
  
  file.save(f)
  
#  do some ML on the file and get classification
  
  classification = "100p a hot dog"
  
  return render_template("test.html", classification = classification)


if __name__ == "__main__":
  app.run(port=5000, debug=True)