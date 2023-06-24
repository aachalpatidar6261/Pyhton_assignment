def factorial(n):
    fac = 1
    for i in range(1,n+1):
        fac = fac*i
    print("The factorial of ",n ," is ",fac)

n = int(input("enter number for factorial : "))
factorial(n)