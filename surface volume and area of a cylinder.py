import math
def volume_cylinder(Pi,r,h):
    volume = Pi * r**2 * h
    return volume

Pi=math.pi
r=2
h=8

print(volume_cylinder(Pi,r,h))

def area_cylinder(PI,r,h):
    area = 2*Pi *r*h + 2*Pi *r**2
    return area
Pi = math.pi
r =2 
h=2
print("area of cylindr : ",area_cylinder(Pi,r,h))
