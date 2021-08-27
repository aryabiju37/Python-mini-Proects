class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1
    def eat(self):
        print("Eat")

    
class Mammal(Animal):
    def __init__(self):
        super().__init__() ##to give a ccess to the super class with the same function name for circumventing method overriting
        print("Mammal Constructor")

    def walk(self):
        print("Walk")

m = Mammal()

