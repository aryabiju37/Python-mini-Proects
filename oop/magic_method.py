from copy import  copy
class Human:
	def __init__(self,first,last,age,height):
		self.first = first
		self.last = last
		self.age = age
		self.height = height

	def __repr__(self):
		return f"Human named {self.first} {self.last}"

	def __len__(self):
		return self.height	

	def __add__(self,other):
		if isinstance(other,Human):
			return Human(first="Babe",last=self.last,age=0,height=33)
		return "You cannot add that"

	def __mul__(self,other):
		if isinstance(other,int):
			return [copy(self) for i in range(other)]
		return ValueError("Expected Human * 2 , order matters")

k = Human("Kevin","Jones",34,188)
j = Human("Jennifer","Florence",26,180)
print((k + j) * 3)

# triplets = j * 3
# triplets[1].first="Janet"
# print(triplets)
# k = Human("Arya","Biju",26,182)
# print(j+k)
# print(len(j))