# This code picks a random food item:
from random import choice #DON'T CHANGE!
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

#DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

# YOUR CODE GOES BELOW:
if food in bakery_stock.keys():
    print(f"{bakery_stock[food]} of {food} left")
else:
    print(f"We don't make {food}")


list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

# make sure your solution is assigned to the answer variable so the tests can work!
answer = {list1[i]:list2[i] for i in range(0,len(list1))}


person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
answer = {person[i][0]:person[i][1] for i in range(0,len(person))  }
print(answer)


# make sure your solution is assigned to the answer variable so the tests can work!
answer = dict.fromkeys([x for x in "aeiou"],0)
answer = dict.fromkeys("aeiou",0)
answer = {char:0 for char in "aeiou"}

# make sure your solution is assigned to the answer variable so the tests can work!
answer = {i:chr(i) for i in range(65,91)}