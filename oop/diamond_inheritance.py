class A:
    def __init__(self):
        pass
    def do_something(self):
        return "A did something"

class B(A):
    def __init__(self):
        pass
    def do_something(self):
        return "B did something"

class C(A):
    def __init__(self):
        pass
    def do_something(self):
        return "C did something"

class D(B,C):
    def __init__(self):
        pass
    def do_something(self):
        return "D did something"

# thing = D()
print(D.__mro__)
print(D.mro())
print(help(D))