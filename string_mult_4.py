def func(str):
    if len(str)%4==0:
        s = str[-1:-len(str)-1:-1]
        print(s)
    else:
        print("string is not multiply by 4")

str = input("enter string for reverse : ")
func(str)
