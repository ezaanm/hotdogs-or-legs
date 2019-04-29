from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def splash():
  return render_template("splash.html")
  
@app.route("/fight", methods=["GET"])
def fight():
  return render_template("fight.html")

@app.route("/test", methods=["GET"])
def test():
  return render_template("test.html")


if __name__ == "__main__":
  app.run(port=5000, debug=True)