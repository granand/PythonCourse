class Animal():

    def __init__(self):
        print("This is an Animal")

    def who_am_I(self):
        print("I am an Animal")

    def eat(self):
        print("Animal eating....")

# Inheritance - Inheriting the Animal class
class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("This is a Dog")
#        Animal.__init__(self)

# method overriding
    def eat(self):
        print("Dog eating....")

    def bark(self):
        print("WOOF! ....")


dog1 = Dog()
# calling super class methods
dog1.who_am_I()
#  overridden method in use
dog1.eat()
# New methods not in parent class
dog1.bark()
