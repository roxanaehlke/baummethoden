import pickle

# Modell laden
model_path = "data/models/model.pkl"
with open(model_path, "rb") as f:
    trained_model = pickle.load(f)

print("Modell geladen.")

# Beispielwerte für eine Prediction
# [zylinder, ps, gewicht, beschleunigung, baujahr]
beispiel = [[6, 133, 3410, 15.8, 78]]

# Prediction
prediction = trained_model.predict(beispiel)

print("Vorhergesagte MPG:", prediction[0])
