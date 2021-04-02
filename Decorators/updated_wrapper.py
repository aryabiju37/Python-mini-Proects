def shout(fn):
    def wrapper(*args,**kwargs):
        return fn(*args,**kwargs).upper()
    return wrapper

@shout
def greet(name):
    return f"Hi my name is {name}"

@shout
def order(main,side):
    return f"Hi, I would like {main} with {side} please."

print(greet("Arya"))
print(order("Burger","Fries"))
