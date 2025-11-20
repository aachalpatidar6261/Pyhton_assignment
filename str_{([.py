str = "{([])}"
# print(type(str))
stack1 = []
stack2 = []
for item in str:
    # print(item)
    if item in "{([":
        stack1.append(item)
    elif item in "])}":
        stack2
    
# print(stack1)

# print(str[0])
l1 = [1,2,3,4,5]
l2 = ["a","b"]
l2.extend(str)
# print(l1,"--- ",l2)

# print("Hello"[::-1])

def SumOfElemet(arr):
    sum = 0
    for element in arr:
        sum +=element
    return sum
arr = [1, 2, 3, 4]
print("With one line sum : ",sum(arr))
print(SumOfElemet(arr))

nums = [1,2,3,41,2,4]
print(nums[::-1])
print(list(set(nums)))

nums = [1, 2, 3]
nums.append([4, 5])
print(nums)
print(len(nums))
print("Python"[::-1])
s = "hello world"
print(s.title())
str = "12345"
s =str.isdigit
print(s)

str = "Write code to count vowels in a string"
count = 0
for item in str:
    if item in "aeiouAEIOU":
        count +=1
print(count)

stack = []
stack.append(10)
stack.append(20)
stack.pop()
print(stack)

stack = [1]
if not stack:
    print("empty")
else:
    print(stack)
st = "madam"
print("Palindrome : ",st == st[::-1])

l1 = []
l1.append(10)
l1.append(20)
l1.pop()
arr = [10, 20, 30]
arr.insert(1, 15)
print(arr)

print(max(arr))
print(15 in arr)
s = "abcde"
print("Reverse string using slicing : ", s[::-1])
print("Length of string using in-bult : ", len(s))

stack = []
for ele in range(0,5):
    stack.append(ele)
print(stack)

s = "hello"
print(s.replace("l", "x")) 
sw = [1,2,3,42,4,5,1,53,2]
from collections import Counter
print("Dic count value (first part) : ",Counter(sw))

dic = {}
for ele in sw:
    if ele in dic:
        dic[ele] +=1
    else:
        dic[ele] = 1
print("Dic count value (second part) : ",dic)

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None