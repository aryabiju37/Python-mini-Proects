import random



user_wish="y"
while(user_wish=="y"):
	random_number = random.randint(1,10)
	user_guess = int(input("Guess a number between 1-10 :"))
	if(user_guess==random_number):
		print("Congratulations you guessed right!")
		
			
	elif(user_guess>random_number):
		print("You guessed too high")
		
	else:
		print("You guessed very low")
		
	user_wish = input("Do you wish or another round? y/n: ")
if user_wish == "n":
	print("Thank you for playing with us!")

	


