instructor = dict(name = "Arya",
					age=25,
					DOB = "21/09/1993",
					is_resourceful=True
				)

#looping through dictionaries
for val in instructor.values():
	print(f"Values in the dictionary are :{val}")

for key in instructor.keys():
	print(f"key:{key}")

for k,v in instructor.items():
	print(f"key is {k} and value is {v}")


#using in with dictionaries

print("name" in instructor)
print("name" in instructor.keys())
#True--checks for keys only


#checking for values 
print("Arya" in instructor)
#gives false , it should be done like below:
print("Arya" in instructor.values())

#fromkeys--assign the same value to an iterbale key
new_dict = dict().fromkeys(["name","place","things","animals"],"None")
print(new_dict)

instructor.get('name')
#"Arya"
email = instructor.get("email")
#email is None --> Truex



#pop vs popitem() in dict:
#pop(key) deletes the value and key associated
#popitem() just deletes values and keys in random

instructor.pop("name")
instructor.popitem()


#update
person = {"City":"Delhi"}
person.update(instructor)
print(person)

#note person.update({}) ie giving an empty dictionary will not change the person dictionary