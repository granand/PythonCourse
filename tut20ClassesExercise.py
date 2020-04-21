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

###########################

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

###########################

class Account:

    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def __str__(self):
        return (f"Account owner: {self.owner} \nAccount balance: ${self.balance}")

    def deposit(self,amt):
        self.balance += amt
        print("Deposit Accepted")

    def withdraw(self,amt):
        if amt > self.balance:
            print("Funds Unavailable!")
        else:
            self.balance -= amt
            print("Withdrawal Accepted")

acct1 = Account('Jose',100)
print(acct1)

print(acct1.owner)

print(acct1.balance)

acct1.deposit(50)

acct1.deposit(100)

acct1.withdraw(75)

print(acct1.balance)

acct1.withdraw(500)

print(acct1.balance)

