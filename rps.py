from random import randint
computer_wins=0
player_wins = 0
winning_count = 2

while computer_wins< winning_count and player_wins< winning_count:
	print("...rock...")
	print("...paper...")
	print("...scissors...")
	print(f"The current win count : Player:{player_wins}, Computer:{computer_wins}")
	player1 = input("(enter your choice): ").lower()
	if player1 == "quit" or player1=="q":
		break
	rand_num = randint(0,2)
	if rand_num == 0:
		computer = "rock"
	elif rand_num == 1:
		computer = "paper"
	else:
		computer = "scissors"


	if player1 == computer:
		print("It's a tie!")

	elif player1 == "rock":
		if computer == "scissors":
			print("Woah you beat the machine")
			player_wins += 1
		else:
			print("computer wins")
			computer_wins += 1


	elif player1 == "paper":
		if computer == "rock":
			print("Woah you beat the machine")
			player_wins += 1
		else:
			print("computer wins")
			computer_wins += 1
		

	elif player1 == "scissors":
		if computer == "paper":
			print("Woah you beat the machine")
			player_wins += 1
		else:
			print("computer wins")
			computer_wins += 1
		
	else:
		print("we only accept rock,paper or scissors as the input")

if computer_wins==winning_count or player_wins==winning_count:
	for r in range(10):
		print("*")
if computer_wins < player_wins:
	print(f"YOU WON THE {winning_count} PART MATCH SERIES AGAINST THE COMPUTER ")
elif computer_wins == player_wins:
	print(f"YOU  TIED THE {winning_count} PART MATCH SERIES WITH THE COMPUTER")
else:
	print(f"OOOOH NOOOOO THE MACHINES ARE OVERTAKING US !!!!!! AI REVOLUTION IS ON  ")
print(f"FINAL SCORE......Player wins : {player_wins}, computer wins: {computer_wins}")


