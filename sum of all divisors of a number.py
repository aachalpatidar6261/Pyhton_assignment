def divisors(num):
    sum = 0
    for i in range(1,num):
        if num%i==0:
            sum +=i
    return sum

num=int(input("enter number, for sum of all divisors of a number: "))
print(divisors(num))
