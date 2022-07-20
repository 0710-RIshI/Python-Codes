import math


class Line:
    def __init__(self,coor1,coor2):
        self.c1=coor1
        self.c2=coor2
    
    def distance(self):
        l=[self.c1[0]-self.c2[0],self.c1[1]-self.c2[0]]
        y=(l[0]*l[0] + l[1]*l[1])
        y=math.sqrt(y)
        print(y)

    def slope(self):
        y=(self.c1[1]-self.c2[1])/(self.c1[0]-self.c2[0])
        print(y)

    

co1=(3,4)
co2=(0,0)

b = Line(co1,co2)

b.distance()
b.slope()




