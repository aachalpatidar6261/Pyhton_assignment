tuple = (1,"a",1.1, 5)
print("Tuple is  : ",tuple)
print(type(tuple))
print("length of tuple : ",len(tuple))

t2 = tuple[-1:-len(tuple)-1:-1]
print("reverse tuple : ",t2)