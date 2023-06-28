class Rectangle:
    def getdata(self,length,width):
        self.length = length
        self.width=width

    def display(self):
        print("area of rectancle : ",self.length*self.width)

rec = Rectangle()
l = int(input("enter length : "))
w = int(input("enter width : "))

rec.getdata(l,w)
rec.display()