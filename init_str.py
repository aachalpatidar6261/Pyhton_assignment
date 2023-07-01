class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        print("init called")
    
    def __str__(self): # return is mandetory
        print("str called")
        return "[{0},{1}]".format(self.x,self.y) # str called that time object is print .
    
    def __add__(self, obj):
        print("add called")
        x=self.x+obj.x
        y = self.y+obj.y
        return Point(x,y)

P1=Point(20,30)
print(P1)
p2=Point(30,40)
print("addition of objects : ",P1+p2)
