a,b = 1,2

print(a+b)
print("module1_add is import to another module(module2.sub)")

# Q26: What does an x = y or z assignment do in Python?
# It assigns the value of y to x if y is truthy; otherwise, it assigns the value of z.
x = 1 or 10  # x will be 10
print(x)
x = 5 or 10  # x will be 5
print(x)