# class Student:

#     def __init__(self,p,c,m):
#         self.p = p
#         self.c = c
#         self.m = m

#     def avg(self):
#         print(self.p+self.c+self.m / 3 )


# s1 = Student(10,10,10)
# s1.avg()

class College_name:
    clg_name = "ABC"
    name = "Empty" # we gave class attribute incase, obj attrbute not gave value of name
    def __init__(self, name):
        print("Diff student name but same clg name, so we initilize clg_name on top of constructor(taki extra memory na jaye)")
        self.name=name

    def method_Welcome(self): #self is necessary
        print("Welcome! Student.", " ", self.name)
col = College_name("Palak")
print(col.name, " ", col.clg_name)
print(College_name.clg_name)
col.method_Welcome()

class Clg:
    def __init__(self, student):
        print("New Student is Added -")
        self.name_student= student
clg = Clg("Aachal")
print(clg.name_student)

class Stud:
    name = "Karan"
    def __init__(self):
        print("Adding New student, without print constructot print bec auto call in python")

st = Stud() # Print construcot line without print 

class Student:
    name = "Karan"
s1 = Student()
print(s1.name)
print(s1)

class Car:
    color = "Blue"
    brand = "BMW"

c = Car()
print(c.color , "  ", c.brand)