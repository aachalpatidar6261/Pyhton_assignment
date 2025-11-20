def fibonacci_sequence(user):
    series = []
    a,b = 0,1
    while a < user:
        series.append(a)
        a,b = b, a+b
        
    return series

user= int(input("Enter Fibonacci Sequence number : "))
print(fibonacci_sequence(user))