import random

list = [1,2,3,4,5,67,78,86,77,44,23]
ra = random.choice(list)
print(" item from a list : ",ra)

tuple = (1,2,3,4,5,67,78,86,77,44,23)
t = random.choice(tuple)
print(" item from a tuple : ",t)

r = random.randrange(30,50)
print("random item from a range : ",r)

r = random.randint(10,100)
print("random number : ",r)
