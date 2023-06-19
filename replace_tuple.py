tup = ("a","b","c","d")
print("tuple : ",tup)
l = list(tup)
l[-1]="e"
tup = tuple(l)
print("after replace last element in tuple : ",tup)
