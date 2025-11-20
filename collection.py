from collections import Counter
list1 = [2,2,3,4,4,2]
b=Counter(list1)
list2=[2,2,3,3,2,2,4]
a=Counter(list2)
list3=[2,2,3,4,4]
# b=Counter(list3)

print(a|b)
print(a&b)
print(b&a)