from random import choice,randint

computer_choice = randint(1,10)
def check(user_in):
    if computer_choice == user_in:
        return "Your guess was right! "
    elif computer_choice < user_in:
        return "you guessed high"
    elif computer_choice > user_in:
        return "you guessed low"

while True:
    user_input = input("Choose a number between 1 and 10: ")
    user_in = int(user_input)
    result=check(user_in)
    print(result)
    if result == "Your guess was right! ":
        user = input("press y to continue n to quit ")
        if user == "n":
            break
        
print("Thanks for playing ")       

    

