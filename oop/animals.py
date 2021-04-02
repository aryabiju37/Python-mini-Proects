class Animal:
    cool = True
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def make_sound(self,sound):
        print(f"this animal makes {sound}")

class Cat(Animal):
    def __init__(self,name,species,breed,toy):
        # self.name = name
        # self.species = species ---code repetition
        #Animal.__init__(self,name,species) -- same thing accomplished by super
        super().__init__(name,species="Cat")
        self.breed = breed
        self.toy = toy
    

blue = Cat("Blue","Persian","Laser light")