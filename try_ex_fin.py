while True:
	try:
		num = int(input("Enter a number: "))
		pass
	except Exception as e:
		print("Thats not a number")
		
	else:
		print("Good job, you entered a number")
		break
	finally:
		print("Prints no matter what")
		pass

print("Rest of game logic")


def divide(a,b):
	try:
		result = a/b
	except(ZeroDivisionError,TypeError) as err:
		print("Something went wrong!")
		print(err)
	else:
		print(f"{a} divided by {b} is {result}")