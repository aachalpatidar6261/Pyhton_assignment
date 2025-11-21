try :
    user = int(input("enter number : "))
    if user%2!=0:
        print("odd number")
except:
    print("not even")
else :
    reciprocal = 1/user
    print("reciprocal : ",reciprocal)




