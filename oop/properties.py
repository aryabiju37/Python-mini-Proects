class Human:

    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        if age >= 0:
            self._age = age
        else:
            raise ValueError("Age cannot be negative")
            
    
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("Age cannot be negative")
    @property
    def full_name(self):
        return "{fname} {lname}".format(fname=self.first,lname=self.last)
    @full_name.setter
    def full_name(self,name):
        self.first,self.last = name.split(" ")


jane = Human("Jane","Goodall",10)
# print(jane.age)
# jane.age = -100
# print(jane.age)
print(jane.full_name)
jane.full_name = "Tim Minchin"
print(jane.__dict__)
