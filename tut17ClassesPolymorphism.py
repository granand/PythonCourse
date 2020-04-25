class Dog:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + "says WOOF! "


class Cat:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + "says MEOW! "


niko = Dog("Niko")
felix = Cat("Felix")

print(niko.speak())
print(felix.speak())

# Polymorphism in play
for pet in [niko, felix]:
    print(type(pet))
    print(pet.speak())

print()


# Polymorphism in play using a method call
def pet_speak(pet):
    print(pet.speak())


pet_speak(niko)
pet_speak(felix)
