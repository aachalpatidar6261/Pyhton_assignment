n = int(input("length of list : "))
l=[]
for i in range(0,n):
    e = input("enter e ")
    l.append(e)
print("list: ",l)

print(type(l))
for i in l:
    l = "{}".format(i)
print("list to string ")
print(type(l))


