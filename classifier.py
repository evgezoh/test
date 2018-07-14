from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

data = pd.read_excel("data.xlsx")
y = data['opsum']
X = data.drop(['opsum'], 1)

clf = RandomForestClassifier(max_depth=2, random_state=0)
clf.fit(X, y)

print(clf.predict(X))

data1 = data[4:]

print(data1)
print(data[data['ID'].isin(data1['ID'])])