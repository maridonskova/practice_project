1. mkdir practice_project
2. cd practice_project && git init
3. mkdir useful_package && touch useful_package/__init__.py
4. git checkout master && git add -A && git 'commit -m 'add init.py'
5. git checkout -b module_a_dev
6. cd .. && touch module_a.py
7. echo "polinom_3 = lambda x: x**3;print(polinom_3(int(input())))" > module_a.py
8. echo "from module_a import polinom_3" > useful_package/__init__.py
9. git add -A && git commit -m "add polinom_3"
10. git checkout master
11. git checkout -b module_b_dev
12. cd .. && touch module_b.py
13. echo "hyperbola = lambda x: 1 / x ; print(hyperbola(int(input())))" > module_b.py
14. echo "from module_b import hyperbola" > useful_package/__init__.py
15. git add -A && git commit -m "add hyperbola"
16. git checkout master && git merge module_a_dev
17. git status, cat __init__.py, nano __init__.py, git add __init__.py, git commit -m "merged and resolved the conflict in __init__.py"
18. git checkout master
19. Create a new repo at github, git clone https://github.com/maridonskova/practice_project
20. git init, it remote add origin https://github.com/artonson/skoltech_fse_v2021.1
21. git push origin master
22. git checkout -b regression-feature 
23. from sklearn.ensemble import RandomForestClassifier
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
24. git add -A && git commit -m "add RandomForestClassifier"
