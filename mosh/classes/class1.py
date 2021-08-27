"""
Define a class in Python, every class method must contain self parameter, while the obect point is being created a pointer will
point self to the new pointer object
"""
# class Point:
#     def draw(self):
#         print("Point Drawn")

# point = Point()
# point.draw()
# print(isinstance(point,Point))

"""
Constructors in python , __init__ method
"""
# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
        
#     def draw(self):
#         print("point ({0},{1})".format(self.x,self.y))

# point = Point(1,2)
# point.draw()

"""
Class vs Instance attribute, class attributes are commomn across all the instances of the class.#Constructor overriding
"""
# class Point:
#     color_given = "Red"
#     def __init__(self,*args):
#         if len(args)==2:
#             self.x ,self.y = args
#         else:
#             self
        
    
#     def draw(self):
#         print("Shape drawn is a point at ({0},{1}) ".format(self.x,self.y))

#     def printy_color(self):
#         print("The color printed is {0}".format(self.color_given))
    
# point = Point(1,2)
# point.draw()
# point.color_given="Yellow"
# point.printy_color()

# point.y= 220
# point.x = 22
# another_point = Point(point.x,point.y)
# another_point.draw()
# Point.color_given="Green"
# another_point.printy_color()

# overriden_point = Point()
# overriden_point.printy_color()

"""
class methods
"""
# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
    
#     def draw(self):
#         print("The point is ({0},{1})".format(self.x,self.y))

#     @classmethod
#     def zero(cls):
#         return cls(0,0)

# point = Point.zero()
# point.draw()

"""
Magic methods
"""
# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
        
#     def __str__(self):
#         return "the point object has constructir values ({0},{1})".format(self.x,self.y)

#     @classmethod
#     def PointInit(cls):
#         return cls(10,299)

    
# point = Point.PointInit()
# print(point)

"""
eq magic method and gt magic method, to compare objects
"""
# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
        
#     def __eq__(self,other):
#         return self.x == other.x and self.y == other.y

#     def __gt__(self,other):
#         return self.x > other.x and self.y>other.y
    
# point = Point(100,200)
# other = Point(10,20)
# print(point > other)

# point = Point(10,20)
# other = Point(10,20)
# print(point == other)

"""
Search web for other magic methods
"""
# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y

#     def __add__(self,other):
#         return "{0},{1}".format(self.x+other.x,self.y+other.y)

# point = Point(10,20)
# other = Point(1,2)   
# combined = point + other
# print(combined.x)

"""
properties
"""
# class Product:
#     def __init__(self,price):
#          self.price = price

#     @property
#     def price(self):
#         return self.__price
    
#     @price.setter
#     def set_price(self,value):
#         if self.__price < 0:
#             print("price cannot be zero")
#         else:
#             self.__price = value

# product = Product(100)
    
"""
Inheritance-and method oerriding  super() - used to access init method of the overriden animal class
"""
# class Animal:
#     def __init__(self):
#         self.age = 1
#         print("Animal Constructor")
    
#     def eat(self):
#         print("eats")


# class Mammal(Animal):
    
#     def __init__(self):
#         self.weight = 55
#         print("Mammal Constructor")
#         super().__init__()


#     def feeds(self):
#         print("infants feed using mammary glands")

# m  = Mammal()
# print(m.age)
# print(m.weight)

# """
# Multi level inheritance and multiple inheritance
# """
# class Animal:
#     def __init__(self):
#         self.age = 1
#         print("Animal constructor")

#     def eat():
#         print("Eat")

    
# class Mammal(Animal):
#     def feeds():
#         print("Younglings feeed using mammary glands")

# class Humans(Mammal):
#     def walks():
#         print("Walks using two hind limbs")

# h = Humans()


# class Employee:
#     def Greet(self):
#         print("Greetings from Employee")

# class Intern:
#     def Greet(self):
#         print("Greetings from Intern")

# class Manager(Intern,Employee):
#     pass

# m = Manager()
# m.Greet()

"""
Inheritance done the right way also abstract classes and methods 

"""
# from abc import abstractmethod
# class InvalidOperationError(Exception):
#     pass

# class Stream(ABC):
#     def __init__(self):
#         self.opened = False

#     def open(self):
#         if self.opened:
#             raise InvalidOperationError("File is already opened")
#         self.opened = True
#     def close(self):
#         if not self.opened:
#             raise InvalidOperationError("File is already closed")
#         self.opened = False

#     @abstractmethod
#     def read(self):
#         pass

# class FileStream(Stream):
#     def read(self):
#         print("Reading data from a file")

# class NetworkStream(Stream):
#     def read(self):
#         print("Reading data from a Network stream")

"""
Polymorphism
"""
# from abc import ABC,abstractmethod
# class UIControl(ABC):
#     @abstractmethod
#     def draw(self):
#         pass

# class TextBox(UIControl):
#     def draw(self):
#         print("Text Box")

# class DropDownList(UIControl):
#     def draw(self):
#         print("Dropdown List")

# def draw(control):
#     control.draw()
# ddl = DropDownList()
# draw(ddl)

# txt = TextBox()
# draw(txt)

