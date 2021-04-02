class Aquatic:
    def __init__(self,name):
        self.name = name

    def swim(self):
        return f"{self.name} is swimming"

    def greet(self):
        return f"I am {self.name} of the sea!"

class Ambulatory:
    def __init__(self,name):
        self.name = name

    def walk(self):
        return f"{self.name} is walking"

    def greet(self):
        return f"I am {self.name} of the land"

class Penguin(Ambulatory,Aquatic):
    def __init__(self,name):
        super().__init__(name)
        #if you are not inheriting using super you need to send the self too
        # Aquatic().__init__(self,name=name)

mister_penguin = Penguin("Mr Penguin")
print(mister_penguin.walk())
print(mister_penguin.swim())
print(mister_penguin.greet())