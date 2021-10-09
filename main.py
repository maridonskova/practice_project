from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import PolynomialFeatures

import numpy as np

from module_a import polinom_3
from module_b import hyperbola

X = np.array(range(-1000, 1000))
trans = PolynomialFeatures(degree=3)
data = trans.fit_transform(X)

print('Print type polinom or hyperbola')
type_f = input()

if type_f == 'polinom': 
    Y = polinom_3(X)
elif type_f == 'hyperbola':
    Y = hyperbola(X)
else:
    print('error type')

clf = RandomForestClassifier(max_depth=4, random_state=0)
clf.fit(data[:-250], Y[:-250])
pred_ = clf.predict(data[-250:])
print(f'MAE is {mean_absolute_error(pred_, Y[-250:])}')

