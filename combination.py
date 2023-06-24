from itertools import product
data = {'1': ['a','b'], '2': ['c','d']} 

for x,y in product(*data.values()):
    print(x+y)
