
a = input("enter ")
b= 0
try :
    c = a/b
    print(c)
except (ZeroDivisionError and TypeError) as e:
    print("error are cought..!!",e)
#xcept TypeError as e:
    print("TypeError..!!",e)
except NameError as e:
    print("NAMEERROR..!!",e)
except SyntaxError as e:
    print("SYNTAXERROR",e)
else:
    print("ERROR...!!")
finally:
    print("Run Program at the END..!!")
