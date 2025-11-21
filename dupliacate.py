l = [1,1,22,4,3,5,22,6]
print(l)
l2 = []
for i in l:
    if i not in l2:
        l2.append(i)
print("after removing duplicate value : ",l2)
    
