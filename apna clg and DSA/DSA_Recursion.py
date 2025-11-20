def factorial(n):
    if n<=1:
        print("return base factorial 1")
        return 1
    print(f"calling factotrial {n-1} inside factoril {n}")
    result = n*factorial(n-1)
    return result

num = int(input("Enter num whose want factorial : "))
print(f"Factorial of {num} : {factorial(num)}")