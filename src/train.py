import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# read csv-file
data = pd.read_csv("data/mpg-data.csv", sep=";")

print(data.columns.tolist())  # Spaltennamen prüfen
print(data.head())  # erste Zeilen prüfen

# Fehlende Werte entfernen
data = data.dropna()

# Features und Zielvariable
x = data[["zylinder", "ps", "gewicht", "beschleunigung", "baujahr"]]
y = data["mpg"]

# Trainings- und Testdaten aufteilen
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

# Modell trainieren
model = LinearRegression()
model.fit(x_train, y_train)

print("Modell trainiert, Score:", model.score(x_test, y_test))

# Speicherordner erstellen falls nicht vorhanden
os.makedirs("data/models", exist_ok=True)

# Modell speichern
model_path = "data/models/model.pkl"
with open(model_path, "wb") as f:
    pickle.dump(model, f)

print("Modell gespeichert unter:", model_path)
