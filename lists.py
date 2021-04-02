words=["programming","is","the","Funniest","thing."]
print(' '.join(words))
name=["Mrs","Arya Sreedhar Dev"]
print('.'.join(name))

colors=["violet","Indigo","Red"]
print(colors[0][0:0:-1])

#"teloiv"

#swapping withibn lists
names = ["James","Alice"]
names[0],names[1]=names[1],names[0]

#list_comprehensions
friends = ["arya","aadi","anant"]
#[_do something__ for x in lists ]
[friend[0].upper()+friend[1:] for friend in friends]

#lc with Conditinal logic
#with single if the syntax is different and with if and else the syntax is different
numbers = [1,2,3,4,5,6,7,8,9,10]
even = [x for x in numbers if x%2 == 0]
odd = [x for x in numbers if x%2!=0]
#else and if
operation = [x/2 if x%2==0 else x*2 for x in numbers]

#list comprehension in string types

vowels= "programming is fun!"
string = ' '.join(char for char in vowels if char not in "aeiou")

#nested_lists
nested_list = [[1,2,3],[4,5,6],[7,8,9]]
[[print(val) for val in l] for l in nested_list]
