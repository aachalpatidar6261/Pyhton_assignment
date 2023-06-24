l = [(101 , "a"),(102,"b"),(103,"c"),(104,"d")]
print(l)

dic = dict(l)  # list to dictionary
print(dic)

di={}
for a, b in l :
    di.setdefault(a, []).append(b)
print(di)