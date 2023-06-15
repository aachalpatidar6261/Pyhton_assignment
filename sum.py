# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

a = int(input("enter a  :"))
b = int(input("enter a  :"))
c = int(input("enter a  :"))

if a==b or b==c or a==c:
    print("sum is zero")
else :
    sum = a+b+c
    print("sum of three interger : ",sum)