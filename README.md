https://github.com/maridonskova/practice_project


1. mkdir practice_project
2. cd practice_project && git init
3. mkdir useful_package && touch useful_package/init.py
4. git checkout master && git add -A && git 'commit -m 'add init.py'
5. git checkout -b module_a_dev
6. cd .. && touch module_a.py
7. echo "polinom_3 = lambda x: x**3;print(polinom_3(int(input())))" > module_a.py
8. echo "from module_a import polinom_3" > useful_package/init.py
9. git add -A && git commit -m "add polinom_3"
10. git checkout master
11. git checkout -b module_b_dev
12. cd .. && touch module_b.py
13. echo "hyperbola = lambda x: 1 / x ; print(hyperbola(int(input())))" > module_b.py
14. echo "from module_b import hyperbola" > useful_package/init.py
15. git add -A && git commit -m "add hyperbola"
16. git checkout master && git merge module_a_dev
17. git status, cat init.py, nano init.py, git add init.py, git commit -m "merged and resolved the conflict in init.py"
18. git checkout master
19. Create a new repo at github https://github.com/maridonskova/practice_project
20. git init, git remote add https://github.com/maridonskova/practice_project
21. git push origin master
22. git checkout -b regression-feature
23.

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


24. git add -A && git commit -m "add main.py"

