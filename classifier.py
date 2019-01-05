from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scikitplot as skplt

data = pd.read_excel("data.xlsx", 'classification')
y = data['opsum']
X = data.drop(['opsum'], 1)

clf = RandomForestClassifier(max_depth=2, random_state=0)
clf.fit(X, y)

print(clf.predict(X))
predict = clf.predict(X)
predict_p = clf.predict_proba(X)
print(predict_p)

y_true = y
y_probas = predict_p
skplt.metrics.plot_roc(y_true, y_probas)
plt.show()

data1 = data[4:]

# print(data1)
# print(data[data['ID'].isin(data1['ID'])])