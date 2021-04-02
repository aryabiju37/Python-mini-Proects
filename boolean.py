age = int(input("How old are you? "))
if age:
	if age >= 21:
		print("You can enter and have a drink ")
	elif age >= 18:
		print("You can enter but with a wrist band")
	else:
		print("You cannot come in, little one! :( ")
else:
	print("Please enter an age!")
