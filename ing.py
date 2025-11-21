s = input("enter string : ")

if len(s)<3:
    print(s)
elif s[-3:]=="ing":
    print("s is ",s.replace(s[-3:],"ly"))
else:
    print(s+"ing")
    