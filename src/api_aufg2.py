from flask import Flask, Response
from flask_cors import CORS

import pandas as pd
import os

app = Flask(__name__)
CORS(app)
# erstellt flask-app


# GET /
@app.route("/", methods=["GET"])
def index():
    return {"hello": "world"}


# gibt json


# GET /hello _world
@app.route("/hello_world")
def hello_world():
    return Response("<p>Hello, World!</p>", mimetype="text/html")


# gibt html


# GET /training_data
@app.route("/training_data")
def training_data():
    file_path = os.path.join(os.path.dirname(__file__), "mpg-data.csv")
    df = pd.read_csv(file_path)
    return df.to_json(orient="records")


# gibt Trainingsdaten als json-array zurück

# Fragen
# Ordner-Struktur selbst erstellen?
# nach "git push" kommt "git push --set-upstream origin DIG-831" müsste "upstram origin nicht main sein?"
#  * [new branch]      DIG-831 -> DIG-831
# branch 'DIG-831' set up to track 'origin/DIG-831'
