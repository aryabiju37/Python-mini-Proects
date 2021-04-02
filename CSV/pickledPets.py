import pickle

class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def make_sound(self,sound):
        print("{self.name} makes {sound}")

class Cat(Animal):
    def __init__(self,name,breed,toy):
        super().__init__(name,species="Cat")
        self.breed = breed
        self.toy = toy

    def play(self):
        print(f"{self.name} plays with {self.toy}")


blue = Cat("Blueberry","Scottish Fold","String")

#pickling an object
#wb=writing binary
# with open("picklecat.pickle","wb") as file:
#     pickle.dump(blue,file)


#unpickling
with open("picklecat.pickle","rb") as file:
    zombie_blue = pickle.load(file)
    print(zombie_blue)
    print(zombie_blue.play())

    


