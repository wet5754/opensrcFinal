import math
class Point:
    x, y = 0, 0
    def __init__(self,a=0,b=0):
        self.x=a
        self.y=b
    
    def distance(self, Point):
        return math.sqrt((self.x-Point.x)**2+(self.y-Point.y)**2)

    def __add__(self,Point):
        return self.x+Point.x,self.y+Point.y


p1 = Point(1,1)
p2 = Point(2,2)

print(p1.distance(p2))
print(p1+p2)