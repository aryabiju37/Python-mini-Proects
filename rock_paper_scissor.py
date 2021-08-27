
from random import choice

Allow = True
user_input = ""
allowed_inputs=["Rock","Paper","Scissors","q"]
def chck_user_input():
    if user_input not in allowed_inputs:
        print("entry not allowed")
        global Allow
        Allow = False
        print("Enter a valid input")
    
def chck_result():
    if computer_input=="Rock":
        if user_input=="Rock":
            return "No one Wins"
        elif user_input=="Paper":
            return "You Won, Congratulations!"
        else:
            return "Computer Wins"
    elif computer_input=="Paper":
        if user_input=="Paper":
            return "No one Wins"
        elif user_input=="Scissors":
            return "You Won, Congratulations!"
        else:
            return "Computer Wins"
    elif computer_input=="Scissors":
        if user_input=="Scissors":
            return "No one Wins"
        elif user_input=="Rock":
            return "You Won, Congratulations!"
        else:
            return "Computer Wins"


print("******Rock*****")
print("******Paper*****")
print("******Scissors*****")   


while(Allow and user_input != "q"):

    user_input = input("Enter your choice:")
    chck_user_input()
    if user_input == "q" or Allow == False:
        break
    computer_input = choice(["Rock","Paper","Scissors"])
    print(f"Computer Inputs : {computer_input}")
    result = chck_result()
    print(result)

    