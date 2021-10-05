from sklearn.ensemble import RandomForestClassifier
import numpy as np
from module_a import polinom_3
from module_b import hyperbola
X = np.random.uniform(low=0.0, high=1.0, size=1000)
if np.random.binominal(1, 0.5): 
    Y = polinom_3(X)
else:
    Y = hyperbola(X)
clf = RandomForestClassifier(max_depth=2, random_state=0)
clf.fit(X, y)
print((clf.predict(input())))
