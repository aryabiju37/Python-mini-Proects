class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"
    @classmethod    
    def zero(cls): #class method we work with the Point class here
        return cls(0,0)

    def draw(self):
        print(f"Point ({self.x},{self.y})")

point = Point.zero()
print(str(point))