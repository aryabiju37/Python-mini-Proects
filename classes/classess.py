class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def draw(self):
        print(f"Point ({self.x},{self.y})")


point = Point(1,2)
print(point.x)
point.draw()
point.z = 10 
point = Point(2,3)
# print(type(point))
# print(isinstance(point,Point))

    