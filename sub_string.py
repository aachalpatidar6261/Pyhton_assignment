# Write a Python program to count occurrences of a substring in a string.

s =input("Enter string : ")
n = input("Enter substring : ")
w = s.split()
sum =0

for i in w:
    if i==n:
        sum+=1
print(sum)
