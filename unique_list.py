l=[1,2,3,1,2,6,5]
print("origin list : ",l)
l2=[]
for i in l:
    if i not in l2:
        l2.append(i)
    
print("unique value : ",l2) 