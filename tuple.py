#immutable
#x[0]=5, not possible
#faster than lists, as the data remains unchanged efficient in coding, can be used as a valid key in dict

x=(1,2,3)

#creating and accessing a tuple:
monate = ("jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec")
print(monate[0])
print(monate[4])

#valid tuples--duplicate values allowed
tup = (1,1,1,2,3,3,3,4,5,5)
tup.count(1)
tup.index(2)#first matching index

#as a key in dict, lists are unhashable types as keys but not tuples
locations = {
	(35.34524,39.4567):"New Delhi Office",
	(12.453654,12.345):"Kochi Office",
	(122.35653,122.3564):"Biscetti"
}
