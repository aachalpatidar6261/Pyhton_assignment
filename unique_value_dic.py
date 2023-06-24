dic ={1: "a", 1:"b",3:"c",4:"a",5:"v"}

dic1={}
for i in dic:
    if dic[i] not in dic1:
        dic1[i] = i
print(dic1)
