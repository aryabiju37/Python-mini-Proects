def triple_and_filter(lst):
 	tripled=[x**3 for x in lst if x%4 != 0]
 	print(tripled)

# print(triple_and_filter([4,3,2,1]))

def tripled(lst):
	trip = map(lambda x:x*3,filter(lambda x: x%4==0,lst))
	return list(trip)

print(tripled([3,4,5,8]))