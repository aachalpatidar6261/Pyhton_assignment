class A:
    def show(self):
        print("class A")
class B(A):
    def show(self):
        super().show()
        print("class B")
class c(B):
    def show(self):
        super().show()
        print("class C")

c = c()
c.show() 