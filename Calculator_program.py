first_num = 70 #int(input())
second_num = 30 #int(input())

num = int(input("Enter 1 for ADD, 2 for SUB, 3 for MULT, 4 for DIV, 5 for MOD : "))

if num == 1:
    print("ADD : ",first_num + second_num)
elif num == 2:
    print("SUB : ",first_num - second_num)
elif num == 3:
    print("MULT : ",first_num * second_num)
elif num == 4:
    print("div : ",first_num / second_num)    
elif num == 5:
    print("ADD : ",first_num % second_num)
else:
    print("wrong enter!")