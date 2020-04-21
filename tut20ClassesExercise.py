class Cylinder:
    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
#      volume = πr2h
        print(Cylinder.pi * (self.radius ** 2) * self.height)

    def surface_area(self):
#       Area=2πrh+2πr2
        print((2 * Cylinder.pi * self.radius * self.height) + ( 2 * Cylinder.pi * self.radius ** 2))

c = Cylinder(2,3)

c.volume()
c.surface_area()


class Line:

    def __init__(self, coor1, coor2):
        self.x1, self.y1 = coor1
        self.x2, self.y2 = coor2

    def distance(self):
#        √ (x2 − x1)2 + (y2 − y1)2
        print(((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)**0.5)


    def slope(self):
#   slope = (y2-y1) / (x2-x1)
        print((self.y2 - self.y1)/(self.x2 - self.x1))

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

li.distance()
li.slope()