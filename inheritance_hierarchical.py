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


b = B()
b.geta(10)
b.puta()
b.getb(20)
b.putb()

c = C()
c.geta(100)
c.puta()
c.getc(300)
c.putc()