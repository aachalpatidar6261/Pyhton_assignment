class A:
    def get(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print("Addition : ",self.a+self.b)
class B(A):
    def sub(self):
        print("Sub : ",self.a-self.b)
    
class C(A):
    def mult(self):
        print("multple : ",self.a*self.b)

class D(B,C):
    def div(self):
        print("division : ",self.a/self.b)



c = C()
c.get(10,2)
c.add()
c.mult()

b=B()
b.get(20,10)
b.sub()

d=D()
d.get(50,5)
d.add()
d.div()