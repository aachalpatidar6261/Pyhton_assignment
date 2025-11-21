class circle:
    def getradius(self,radius):
        self.radius=radius

    def area_circle(self):
        print("area of circle : ",3.14*self.radius**2)
    
    def perimeter_circle(self):
        print("perimeter of circle : ",2*3.14*self.radius)
    
circle = circle()
radius = int(input("enter radius : "))
circle.getradius(radius)
circle.area_circle()
circle.perimeter_circle()