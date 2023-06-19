def intersection(l1, l2):
    a =set(l1)
    b = set(l2)
    
    
    if a&b:
        print("common",a&b)
        return True
    else:
        print("not common",a&b)
        return False


n = int(input("enter length of list l1 and l2 : "))
l1 = []
for i in range(0,n):
    e = int(input("enter e for l1 : "))
    l1.append(e)


l2 = []
for i in range(0,n):
    e = int(input("enter e for l2 : "))
    l2.append(e)

print("l1 : ",l1)
print("l2 : ",l2)
intersection(l1, l2)




