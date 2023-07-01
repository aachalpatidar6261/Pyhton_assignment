class A:
    def geta(self,a):
        self.a=a
    def puta(self):
        print("class A : ",self.a)
class B:
    def getb(self,b):
        self.b=b
    def putb(self):
        print("class B : ",self.b)
class C(A,B):
    print("Class C : This is derived class of A and B.")

c1 = C()
c1.geta(10)
c1.puta()
c1.getb(20)
c1.putb()

