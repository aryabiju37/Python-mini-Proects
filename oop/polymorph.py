class Animal():
    def speak(self):
        return NotImplementedError("Sub classes must implement this method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow"

class Fish(Animal):
    def speak(self):
        pass
    pass

d = Dog()
print(d.speak())
f = Fish()
print(f.speak())