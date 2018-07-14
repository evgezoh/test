import pandas as pd
import numpy as np
import scipy.stats
from sklearn.cluster import KMeans
from sklearn import mixture
from sklearn.ensemble import RandomForestRegressor


def mae(y, y_pred):
    return np.sum(np.abs(y - y_pred)) / len(y)


def mape(y, y_pred):
    return np.sum(np.divide(np.abs(y - y_pred), y)) / len(y)


def RSQ(y, y_pred):
    sum_mod = np.sum((y - y_pred) ** 2)
    sum_y = np.sum((y - np.mean(y)) ** 2)
    return 1 - sum_mod / sum_y


def Fisher(y, y_pred, imp, rsq):
    f_1 = len(np.where(imp != 0)[0])
    f_2 = len(y_pred) - f_1 - 1
    if rsq != 1 and f_1 != 0:
        return rsq * f_2 / (f_1 * (1 - rsq)), scipy.stats.f.ppf(q = 1 - 0.05, dfn = f_1, dfd = f_2)
    else:
        return 0, 0


def answer(y, y_pred):
    div_pred = np.divide(y, y_pred)

    _75 = len(np.where(div_pred < 0.75)[0]) / len(y)
    _125 = len(np.where(div_pred > 1.25)[0]) / len(y)
    _75_125 = 1 - _75 - _125

    return _75, _75_125, _125



data = pd.read_excel("data.xlsx").drop(['ID'], 1)

kmeans = KMeans(n_clusters = 3, random_state = 0)
kmeans.fit(data)

mix = mixture.GaussianMixture(n_components = 5, max_iter= 10000)
mix.fit(data)

list = kmeans.predict(data)
list = mix.predict(data)

data['cluster'] = list

writer = pd.ExcelWriter('output.xlsx')
data.to_excel(writer, "Sheet1")
writer.save()

y = data['opsum']
data = pd.read_excel("data.xlsx").drop(['ID', 'opsum'], 1)

_75_125_ = 0
estim = 1
featur = 2

for trees in range(100, 120):
    for features in range(2, 5):
        regr = RandomForestRegressor(n_estimators=trees, max_features= features, min_samples_leaf= 2, random_state=0)
        regr.fit(data, y)

        y_pred = regr.predict(data)
        imp = regr.feature_importances_

        _75, _75_125, _125 = answer(y, y_pred)

        if _75_125 > _75_125_:
            _75_125_ = _75_125
            estim = trees
            featur = features

        print(_75, " ", _75_125, " ", _125)
        #print(mae(y, y_pred))
        #print(mape(y, y_pred))

print(estim)
print(featur)

regr = RandomForestRegressor(n_estimators=estim, max_features=featur, min_samples_leaf=2, random_state=0)
regr.fit(data, y)

y_pred = regr.predict(data)
imp = regr.feature_importances_

print("MAE: ", np.round(mae(y, y_pred)))
print("MAPE: ", np.round(mape(y, y_pred) * 100, 2), "%")
print("RSQ: ", np.round(RSQ(y, y_pred), 2))
print("Fisher, Fisher_crit: ", np.round(Fisher(y, y_pred, imp, RSQ(y, y_pred)), 2))
print(np.round(answer(y, y_pred), 2))


control = pd.read_excel("data.xlsx", sheet_name='control').drop(['ID'], 1)
y = control['opsum']
control = control.drop('opsum', 1)
regr.predict(control)