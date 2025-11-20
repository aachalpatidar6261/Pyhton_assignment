l = [21,23,87,98,663,777,2,2,3,21,246,75,57,3]
print(min(l))
s = l[0]
lar = l[0]
for item in l:
    print
    if item < s:
        s = item
    if item > lar:
        lar = item
print("Smallest Element : ",s)
print("Largest Element : ",lar)

print("REverse list : ",l[::-1])
print("ount element in list : ",len(l))
count = 0
for item in l:
    count+=1
print("cout element in list without function : ",count)
l.sort()
print("Increasing order : ",l)
l.sort(reverse=True)
print("Decreasing order : ",l)
# Increasing = []
# num = l[0]
# for item in l:
#     if 
sum = 0
for i in l:
    sum+=i
print("Sum of all element : ",sum)
# odd enevn pr or even odd pr
print("Average of all elements : ", sum / count)
# print("Remove duplicate : ",list(set(l)))
l.append(888)
print("Add element : ",l)

s = "rabar"
r_s = s[::-1]
for i in s:
    for j in r_s:
        if i == j:  
            print(s, "yes")
        else:
            print(s, "no")

def discounted(price, discount):  
    return price * (1 - discount / 100)

nums = (55, 44, 33, 22)
print(nums[:2][-1])

def apply_twice(func, arg):
    return func(func(arg))

def add_five(x):
    return x + 5

print(apply_twice(add_five, 10))
print(len("Python Developer with 1 year of experience in Django, DRF, REST APIs, Shopify, and building scalable web apps and creative backend solutions."))