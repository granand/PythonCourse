class Animal():

    def __init__(self,name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

class Dog(Animal):

# Note here we didn't have the __init__ class here we can make use of the __init__ from parent class

    def speak(self):
        return self.name + "says WOOF! "

class Cat(Animal):

    def speak(self):
        return self.name + "says MEOW! "


#myanimal = Animal("Fred")
# Throws an error as we are not suppose to use it this way
#myanimal.speak()

niko = Dog("Niko")
felix = Cat("Felix")

print(niko.speak())
print(felix.speak())

