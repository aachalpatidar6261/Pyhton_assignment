# INHERITANCE - 
# Creating new class from an existing class is called inheritance.

# single Inheritance 

class A :
    def get(self,a):
        self.a=a
    def put(self):
        print("class A : ",self.a)
class B(A):
    def getb(self,b):
        self.b=b
    def putb(self):
        print("class B : ",self.b)
B1=B()
B1.get(10)
B1.getb(20)
B1.put()
B1.putb()