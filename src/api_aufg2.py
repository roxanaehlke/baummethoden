from flask import Flask, Response, request
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

# Aufgabe 3: mpg-Modell


# GET /predict
# Beispiel: /predict?zylinder=6&ps=133&gewicht=3410&beschleunigung=15.8&baujahr=78
@app.route("/predict")
def predict():
    # URL-Parameter auslesen
    zylinder = request.args.get("zylinder")
    ps = request.args.get("ps")
    gewicht = request.args.get("gewicht")
    beschleunigung = request.args.get("beschleunigung")
    baujahr = request.args.get("baujahr")

    # Als DataFrame übergeben (vermeidet UserWarning)
    beispiel = pd.DataFrame(
        [
            [
                float(zylinder),
                float(ps),
                float(gewicht),
                float(beschleunigung),
                float(baujahr),
            ]
        ],
        columns=["zylinder", "ps", "gewicht", "beschleunigung", "baujahr"],
    )

    file_path = os.path.join(os.path.dirname(__file__), "..", "data", "mpg-data.csv")
    data = pd.read_csv(file_path, sep=";")

    # Prediction — nur erstes Element der Liste zurückgeben
    prediction = trained_model.predict(beispiel)

    return {"result": prediction[0]}
