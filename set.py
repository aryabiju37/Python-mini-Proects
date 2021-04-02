#unique values, unordered, hence not accessible using index

egpl = {1,2,3,4,5,21,32,34,45."a"}
print("a" in egpl)
#True

# 1 - Create a variable called numbers which is a tuple with the the values 1, 2, 3 and 4 inside.
numbers=(1,2,3,4)

# 2 - Create a variable called value which is a tuple with the the value 1 inside.

value=(1,)
# 3 - Given the following variable:

values = [10,20,30]

# Create a variable called static_values which is the result of the values variable converted to a tuple

static_values= tuple(values)
# 4 - Given the following variable

stuff = [1,3,1,5,2,5,1,2,5]

# Create a variable called unique_stuff which is a set of only the unique values in the stuff list
unique_stuff = set(stuff)

#set comprehensions
{x**2 for x in range(0,10)}

{char.upper() for char in "Hello"}