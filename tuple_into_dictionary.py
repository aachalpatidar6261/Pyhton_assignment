tuple = ((1, "a"),(2,"b"),(3,"c"),(4,"d"))
dic = {}
for a,b in tuple:
    dic.setdefault(a,[]).append(b)
print(dic)
