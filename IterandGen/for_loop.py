# def my_for(iterable):
# 	iterator = iter(iterable)
# 	while True:
# 		try:
# 			print(next(iterator))
# 		except StopIteration:
			
# 			break

# my_for("Hello From the other side!")


##what happens inside a for loop::

def my_for(iterable,func):
	iterator = iter(iterable)
	while True:
		try:
			thing = next(iterator)
		except StopIteration:
			
			break
		else:
			func(thing)



def square(x):
	print(x**2)

my_for([1,2,3],square)
print(my_for("Hello",print))