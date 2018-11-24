from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import json
import base64
import datatoimage
app = Flask(__name__)
CORS(app)


@app.route("/api/create", methods=["POST"])
def receiveData():
    with open("test.jpg", "wb") as f:
        f.write(base64.b64decode(request.json["image-data"]))
    data = datatoimage.dataToImage(request.json.pop("image-data"), request.json)
    with open("test2.bmp", "wb") as f:
        f.write(base64.b64decode(data))
    return data


@app.route("/", methods=["GET"])
def index():
    html = ""
    with open("index.html", "r") as f:
        html = f.read()
    return html

@app.route("/create", methods=["GET"])
def create():
    html = ""
    with open("create.html", "r") as f:
        html = f.read()
    return html

@app.route("/image", methods=["POST"])
def returnImage():
    return render_template('image.html', imagedata = request.form["image-data"])
