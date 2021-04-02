
def speak(animal="dog"):
"""returns the sound that the animal makes defaulted to the dog sound"""
    spaketh_who = dict(pig="oink",
                    duck="quack",
                    cat="meow",
                    dog="woof")
    noise=spaketh_who.get(animal)
    if noise :
        return noise
    else:
        return "?"
   print(speak__docstring__)

def add(a,b):
	return a+b

def sub(a,b):
	return a-b
def func(fn=add,a,b):
	return fn(a,b)