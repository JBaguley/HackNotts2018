from flask import Flask, request, jsonify
import json
import base64
app = Flask(__name__)


@app.route("/api/create", methods=["POST"])
def receiveData():
    with open("test.jpg", "wb") as f:
        print(request.json)
        f.write(base64.b64decode(request.json["image-data"]))
    return "Got it!"