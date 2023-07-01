class A:
    def show(self):
        print("class A")
class B(A):
    def show(self):
        print("class B")
class c(B):
    def show(self):
        print("class C")

c = c()
c.show() # Derived class override the base(a and b) class.