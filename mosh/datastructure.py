##lists
# letters = ["a","b","c"]
# matrix = [[10,20,3],[3,4]]
# print(matrix)
# zeros = [0]*20
# print(zeros)
# ones = [1]*5
# print(ones)
# fives = [5]*5
# print(fives)
# combined = zeros+letters
# print(combined)
# numbers = list(range(20))
# print(numbers)
# chars = list("Python prog")
# print(chars)
##length of a list
# length = len(chars)
# print(length)

##list unpacking - the number of variables must equal the number of elements in the list

# lists = [1,2,3,4]
# first,second,third,fourth = lists
# print("The unpacked list is {} ,{} ,{} and {}".format(first,second,third,fourth))

# numbers = list(range(4))
# first,second,*others = numbers
# first,*others,last = numbers
# print(first,others,last)

# numbers = ["num1","num2","num3"]
# #enumerate to get the index of the list
# for index,num in enumerate(numbers):
#     print("Number {} at index {}".format(num,index))
# # enumerate returns a tuple
# for n in enumerate(numbers):
#     print(n)

#letters = ["a","b","c"]

# #Add

# letters.append("d")
# # Add a particular item to the particular index
# letters.insert(0,"A")
# print(letters)


# #delete 

# #pop(index) deletes one item based on the index provided
# popped = letters.pop(1)
# print(popped)

# #del deletes a range of items from the list
# del letters[0:3]
# print(letters)

# #removes the first occurence of "b", remaining b's should be removed by looping over the list
# letters.remove("b")
# print(letters)

# #Clear all the items from the list
# letters.clear()
# print(letters)

## Find

# letters = ["a","b","c"]
# letters.index("d")
##.index method gives an error if the indexed item is not present in the list,this behaviour is different to the C based progs that gives a -1 upon not finding the list item.
##instead of getting an error, rewrite the index method as:

# if "d" in letters:
#     print(letters.index("d"))
## or get the count of the number of occurences of "d" in the list
# print(letters.count("d"))



# numbers = [3,51,2,8,6]
## ascending sort 

##Sort method sorts the list in ascending or descending order changing the original list
# numbers.sort()
# print("Ascending Sort is: {0}".format(numbers))

##descending sort
# numbers.sort(reverse=True)
# print("Descending sort is : {0}".format(numbers))

## sorted-method does not change the original list:
# numbers_actual = [3,65,100,99,83,73,12,1]
# sorted_nums=sorted(numbers_actual,reverse=True)
# print(sorted_nums)


##Sorting the list of tuples or list of lists eg: product list with several description based on price, quality,ratings etc 
# items = [
#     ["Shampoo",105,{"rating":3}],
#     ["conditioner",37,{"rating":4}],
#     ["Soap",57,{"rating":3.5}]
# ]
# # unsorted_list =  items.copy()

# # def sort_items_by_price(item):
# #     return item[1]


"""
you call items.sort(), so the argument to the sort_items
 methods would be item; list not items , the list of lists
"""
# def sort_items_by_rating(item):
#     return item[2]["rating"]

# # sort_items_by_price
# items.sort(key=sort_items_by_rating)
# print(items)

## lambda functions

# items = [
#     ["Shampoo",105,{"rating":3}],
#     ["conditioner",37,{"rating":4}],
#     ["Soap",57,{"rating":3.5}]
# ]
## unsorted_list =  items.copy()
##items.sort(key = lambda params:expression)

# items.sort(key = lambda item:item[1])
# print(items)

## Map functions
"""
requirement : get the price of items from the list of items and put it in a separate list
"""
items = [
    ["Shampoo",105,{"rating":3}],
    ["conditioner",37,{"rating":4}],
    ["Soap",57,{"rating":3.5}]
]

##naive way :
# item_price = []
# def get_price(items):
#     for item in items:
#         item_price.append(item[1])
#     return item_price

# prices = get_price(items)
# print(prices)

##iterate over one or more iterables
## map returns an iterable object
# mapped_prices = list(map(lambda item:item[1],items))

## Filter function 
# filtered_prices = list(filter(lambda item:item[1]>40,items))
# print(filtered_prices)
 
## list comprehension
"""
[selection for expression(loops mostly)]
"""

# prices = [item[1] for item in items if item[1]>40]
# print(prices)

##Zip function 
# list1 = [1,2,3]
# list2 = [10,20,30]

# zipped_lst = list(zip(list1,list2))
# print(zipped_lst)


##Stacks - LIFO
# browsing_session = []
# browsing_session.append(1)
# browsing_session.append(2)
# browsing_session.append(3)
##Check stack not empty , if not empty pop()
# if browsing_session:
#     last = browsing_session.pop()
#     print("The last item popped with LIFO is {}".format(last))
# if not browsing_session:
#     print("Empty stack")
# redirected_page_num = browsing_session[-1]
# print("redirected on back press to {}".format(redirected_page_num))

##Queue
##FIFO

# queue = []
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.append(4)
# queue.append(5)
# ##pop
# if queue:
#     del queue[0]

# elif not queue:
#     print("Empty queue")

# print(queue)


## Tuple
# point = 1,2
# print(point)

# point1 = (3,4)
# print(point1)

# ##concatenating tuples
# point2 = point + point1
# print(point2)

# ##converting list to tuple:
# point = tuple([1,2,3])
## Tuple unpacking
# x,y,z,i = point2
# print("Tuple unpacked values: x,y,z,i= {},{},{},{}".format(x,y,z,i))
# ##indexing
# print(point[1:3])

# x = 10
# y = 12
# print("X and Y before swap : {},{}".format(x,y))
# tmp = x
# x = y
# y = tmp

# print("X and Y after the swap : {x},{y}".format(x=x,y=y))

##Sets 
# numbers = [1,1,1,2,3,4,5]
# unique = set(numbers)
# print(unique)
# second = {1,4}
# second.add(5)
# first = {1,1,2,3,4,5}
# second = {3,4,5,6,7,8,9,10}
# print("first or econd: {} ".format(first | second))
# print("first set minus second set {}".format(first - second))
# print("first & second - ie elements in first as well as second {}".format(first & second))
# print("first ^ second ie elemenst in both first and second would be eliminated {}".format(first ^ second))

##Dictionaries
# point = dict(x=1,y=2)
# point = {"x":12,"y":11}

# print(point["x"])
# point["x"]=21
# print(point)

# if "a" in point:
#     print(point["a"])

##get method returns none if the key not in dictionary else you can also provide a deafault value to be returned 
# print(point.get("a"))
# print(point.get("a",0))

##iterate over the dictionary
# for key in point:
#     print(key,point[key])
##another method for iterating over dictionaries, returns a tuple so we can unpack the tuple in the beginning of the for loop

# for items in point.items():
#     print(items)

# for key,value in point.items():
#     print(key,value)

##Dictionary Comprehensions
# values = {x:x**2  for x in range(1,5)}
# print(values)

##Generator objects

##generators are also iterables, they spit out values only when looping through a for loop.

# from sys import getsizeof
# values = ( x for x in range(1000000))
# for x in values:
#     print(x)
# list_val = [x*2 for x in range(100000)]
# print("generator size: {}".format(getsizeof(values)))
# print("List size :{}".format(getsizeof(list_val)))

##Unpacking operators; unpack any iterable
# numbers = [1,2,3,4,5]
# print(1,2,3,4,5)
# print(*numbers)

# values = [*range(5)]
# print(values)

# str_unpack = [*"Hello World"]
# print(str_unpack)

# """
# combine dictionaries, if , combined has keys of the same value the last key will be used,in the given example
# x:1 is in the combined dict instead of x:10
# """
# first = {"x":10}
# second = {"x":1,"y":2}
# combined = {**first,**second,"z":3}
# print(combined)





