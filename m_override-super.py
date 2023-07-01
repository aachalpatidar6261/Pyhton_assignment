class A:
    def show(self):
        print("class A")
class B(A):
    def show(self):
        super().show()      # 2
        print("class B")
class c(A):
    def show(self):
        super().show()      # 3
        print("class C")

class D(B,c):
    def show(self):
        super().show()      # 1
        print("class D")


d= D()
d.show()  # flow -> D > B > C > A