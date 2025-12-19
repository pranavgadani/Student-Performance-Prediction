import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression 
import pickle

data = pd.read_csv("dataset.csv")

X = data.drop("result", axis=1)
y = data["result"]

model = LogisticRegression()
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))
