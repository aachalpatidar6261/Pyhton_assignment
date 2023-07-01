class A:
    def geta(self,a):
        self.a=a
    def puta(self):
        print("class A : ",self.a)
class B(A):
    def getb(self,b):
        self.b=b
    def putb(self):
        print("class B : ",self.b)
class C(A):
    def getc(self,c):
        self.c=c
    def putc(self):
        print("class c : ",self.c)

class D(B,C):
    def getd(self,d):
        self.d=d
    def putd(self):
        print("class D : ",self.d)

d = D()
d.geta(10)
d.puta()
d.getb(20)
d.putb()
d.getc(30)
d.putc()
d.getd(40)
d.putd()