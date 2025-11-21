def prime(n):
    if n%2!=0:
        for i in range(3, int(n/2)+1,2):
            if n%i==0:
                print("not prime")
                break
        else:
            print("Prime")
            
    else:
        print("not prime")

n = int(input("enter number : "))
prime(n)