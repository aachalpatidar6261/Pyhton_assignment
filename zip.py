""" The zip() function in Python is commonly used to combine two or more iterables, such as lists,
 tuples, or strings, into a single iterable where elements from corresponding positions are paired together. """

l1 = ["a","b","c"]
l2 =[1,2,3]
zipped = zip(l1,l2)
print(zipped)   # zip gave output in hexadecimal 
print("zip : ",list(zipped))

# list to dictionary

dic = {i:j for i,j in zip(l1,l2)}
print("two list in dictionary by zip : ",dic)
print(type(dic))