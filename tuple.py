tuple = (1,"a",1.1, 5,1,True)
print("Tuple is  : ",tuple)
print(type(tuple))
print("length of tuple : ",len(tuple))

t2 = tuple[-1:-len(tuple)-1:-1]
print("reverse tuple : ",t2)
print("count 1 : ",tuple.count(1)) # True == 1 , False==0
print("index of 5 : ",tuple.index(5))
