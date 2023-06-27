def trapezoid(base1, base2,height):
    area = (base1+base2)/2*height
    return area

base1 =int(input("enter value of base1: "))
base2 =int(input("enter value of base2: "))
height=int(input("enter value of height: "))
print("area of Trapezoid : ",trapezoid(base1,base2,height))