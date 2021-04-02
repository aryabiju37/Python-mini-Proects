def be_polite(fn):
    def wrapper():
        print("Hello, how are you")
        fn()
        print("My darling today?")
    return wrapper

@be_polite
def greet():
    print("Arya")

@be_polite
def rage():
    print("Alavaladi")

print(greet())