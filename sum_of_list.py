l = []
n = int(input("enteer length of list : "))
for i in range(n):
    ele=int(input("enter element : "))
    l.append(ele)
print("list : ",l)

l.sort()
print("sort : ",l)
print("the largest number : ",l[-1])
print("the smallest number : ",l[0])


sum =0 
for i in l:
    sum = sum+i
print("sum of all list element :",sum)
