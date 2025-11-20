#print("main")
# print(input("Eter : "))5
def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()


print (0.1 + 0.2 == 0.3)

print("""Jante huwe bhi anjaan bante ho,
Kuch is tarah hume pareshan krte ho,
puchte ho humse ki hame ky Taklif hai,
Jawab khud hokar bhi humse sawal krte ho.""")

d={'value1': 'value1', 'value2': 'multi'}
print(d['value1'])

"""
Reverse a String. ...
Check if a number is even or odd: ...
Print all factors of a number: ...
Calculate the factorial of a number: ...
Swap two numbers without using a temporary variable: ...
Check if a string is a palindrome: ...
Find the sum of all elements in a list.
"""