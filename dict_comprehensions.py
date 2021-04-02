numbers = dict(first=1,
				second=2,
				third=3
			)	

squared_numbers = {key:value**2 for key,value in numbers.items()}		
print(squared_numbers)

print({num: num ** 2 for num in [1,2,3,4,5]})

str1 = "123"
str2 = "ABC"
combo = {str1[i]:str2[i] for i in range(0,len(str1))}
print(combo)

instructor = dict(name="Colty",
					is_resourceful="Yes",
					city="Munich",
					fav_color="Red"

	)
yelling_instructor = {k.upper():v.upper() for k,v in instructor.items()}
print(yelling_instructor)

num_list= [1,2,3,4,5]
evn = {num:("even" if num%2==0 else "odd") for num in num_list}
print(evn)

yelling_instructor = {(k.upper() if k=="fav_color" else k):v.upper() for k,v in instructor.items()}
print(yelling_instructor)

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = {person[i][0]:person[i][1] for i in range(0,len(person))  }
print(answer)