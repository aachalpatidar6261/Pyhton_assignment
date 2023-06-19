n = int(input("enter lenth of list : "))
l=[]

for i in range(n):
    ele = input("enter element : ")
    l.append(ele)
print("list : ",l)
print("list [-1] is : ",l[-1])


l.pop()
print("after removed last element in list : ",l)
print("list [-1] is : ",l[-1])