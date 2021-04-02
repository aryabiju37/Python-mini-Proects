class GrumpyDIct(dict):
	def __repr__(self):
		print("None Of Your Business")
		#the super class here would be the dictionary
		return super().__repr__()
		
	def __missing__(self,key):
		print(f"You want {key}, well it ain't here!")


	def __setitem__(self,key,value):
		print("You want to change the value of the dictionary???")
		print("Ugh, fine...")
		return super().__setitem__(key,value)

data = GrumpyDIct({"first":"Tom","animal":"Cat"})
print(data)
data['city']="Tokyo"
print(data)