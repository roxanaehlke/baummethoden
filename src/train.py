import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# read csv-file
data = pd.read_csv("data/mpg-data.csv", sep=";")

print(data)
