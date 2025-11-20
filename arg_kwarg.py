def example(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

example(1, 2, a=3, b=4)

import pickle

# Pickling
data = {'key': 'value'}
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

# Unpickling
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

# find sum of 2 to 10

def sum(a,b,*args):    
    s=1
    for item in args:
        s+=item
    return s

s = sum(1,2,3,4,5,6,7,8,9,10)
print("sum of 1 to 10 by args : ",s)

a=3
print("a<<1 : ",a<<1)

class Car:
    def __init__(self):
        self.name = "swift"
        self.maxspeed = 150

c = Car()
c.name="Wagon R"
c.maxspeed=135

print("Name : ",c.name,", MaxSpeed : ",c.maxspeed)

# Replace word

print("Hello".replace("l","e"))

li = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
for j in range(4):
    for ele in li:
        print(ele[j],end=" ")

print(" ")
a=2
b=4
c = a & b
print(" a & b : ",c)

a= "abce">="abcdef"
print(a)

