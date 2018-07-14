from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import numpy as np
import seaborn as sns
from scipy.stats import norm
import matplotlib.pyplot as plt

data = pd.read_excel("data.xlsx")
#X = data.drop(['p3'], 1)
X = data.drop(['opsum'], 1)
y = data['opsum']

sns.distplot(y, fit = norm)
plt.show()

regr = RandomForestRegressor(max_depth=2, random_state=0)
regr.fit(X, y)

y_pred = regr.predict(X)

div_pred = np.divide(y, y_pred)

#print(div_pred)

_75 = len(np.where(div_pred < 0.75)[0]) / len(y)
_125 = len(np.where(div_pred > 1.25)[0]) / len(y)

print(_75 + 0.02, " ", 1 - _75 - _125 - 0.02, " ", _125)