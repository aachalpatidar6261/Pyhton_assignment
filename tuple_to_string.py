n = int(input("enter length of tuple : "))
l =[]
for i in range(0,n):
    ele = input("enter element for tuple : ")
    l.append(ele)
t = tuple(l)
print(type(t))


for i in t:
    s = "{}".format(i)
print("Tuple to string : ")
print(type(s))   
