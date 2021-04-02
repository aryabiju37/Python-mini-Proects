#takes in tuple
def sum_of_all_nums(*args):
	print(type(args))
	sum=0
	for num in args:
		sum += num
	return sum

print(sum_of_all_nums(1,2,3,4,5))




#returns a dictionary
def fav_colors(**kwargs):
	for person,color in kwargs.items():
		print(f"{person}'s favorite color is {color}")

fav_colors("Purple",ruby="Red",ethel="Teal")