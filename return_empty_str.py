def fun(st):
    
    a = st[0:2]
    b = st[-2:]

    if len(st)<2:
        print("Empty string")
    else:
        print(a+b)
fun(st = input("enter string : "))