def sum_of_all_list(*args):
	sum = 0 
	for num in args:
		sum+= num
	return sum

num = [1,2,3,4,5,]
#print(sum_of_all_list(num))----- gives error
print(sum_of_all_list(*num))

def display_names(a,b,c,**kwargs):
	print(a+b*c)
	print("OTHER STUFF")
	print(kwargs)

data = dict(a=1,b=2,c=3,d=55,name="Rya")
print(display_names(**data,cat="Snuggles"))

