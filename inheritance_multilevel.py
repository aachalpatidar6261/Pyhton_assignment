class A:
    def getA(self,a):
        self.a=a
    def puta(self):
        print("class A : ",self.a)
class B(A):
    def getB(self,b):
        self.b=b
    def putb(self):
        print("class B : ",self.b)
class c(B):
    def getc(self,c):
        self.c=c
    def putc(self):
        print("class C : ",self.c)

c1 = c()
c1.getA(10)
c1.puta()
c1.getB(20)
c1.putb()
c1.getc(30)
c1.putc()
