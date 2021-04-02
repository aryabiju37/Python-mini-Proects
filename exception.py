def Colorize(text,color):
	colors = ("cyan","yellow","red","magenta")
	if type(text) is not str:
		raise TypeError("text must be an instance of str")
	if color not in colors:
		raise ValueError("Color is invalid color")
	print(f"Printed {text} in {color}")


Colorize("hello","red")
Colorize(123,"magneto")


try:
	foo_bar
except:
	print("Problem!")
print("after the try")

def get(d,key):
	try:
		return d[key]
	except KeyError:
		return None

d = {"name":"Ricky"}
print(get(d,"city"))
