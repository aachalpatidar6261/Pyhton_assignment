def li(l):
    l2=[]
    for i in l:
        if i not in l2:
            l2.append(i)
    print("remove duplicate value in list using function ",l2)


l = [1,2,3,41,3,5,2,3]
print("original list ",l)
li(l)

