# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

s1 = input("enter 1st string : ")
s2 = input("enter 2nd string : ")

a=s1.replace(s1[0:2],s2[0:2])
b=s2.replace(s2[0:2],s1[0:2])

print(a+ " " + b)