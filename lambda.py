def square(num):
	return num*num
square2 = lambda num: num**2
print(square2(7 ))

add = lambda a,b:a+b 

#map a functioon and an iterable
nums=[1,2,3,4,5]
squares = map(square,nums)
print(list(squares))

#the above fn can be replaced with lambdas as:
nums=[10,9,8,7,6]
squaress = map(lambda num:num**2,nums)
print(list(squaress))
 
# names = dict(first="Colt",last="Steeld",
# 	first="arya",last="biju",
# 	first="Sreedhar",last="biju")#error duplicte key error
first = list(map(lambda x:x["first"],names))