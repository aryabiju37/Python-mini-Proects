import random
random_number = random.randint(1,10)

while True:
	guess = int(input("Enter a number between 1-10: "))
	if guess < random_number:
		print("Too Low!")
	elif guess > random_number:
		print("Too High!")
	else:
		print("You guessed right!")
		choice = input("Do you wish to continue?y/n: ")
		if choice=="y":
			random_number=random.randint(1,10)
		else:
			print("Thank you for playing with us")

