def perfect(n):
    sum = 0 
    for i in range(1,n):
        if n % i ==0:
            sum +=i
    return sum==n
n = int(input("enter number for check a number is perfect or not "))
print(perfect(n))