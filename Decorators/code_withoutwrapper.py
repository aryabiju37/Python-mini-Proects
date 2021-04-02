def be_polite(fn):
    def wrapper():
        print("Hello how are you")
        fn()
        print("My darling today?")
    return wrapper

def greet():
    print("Arya , deedee")

def rage():
    print("Alavalaadi")

greet = be_polite(greet)
age = be_polite(rage)
print(age())
print(greet())

