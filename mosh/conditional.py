# #****************************** Conditional statements***************************
# temperature = 14
# if temperature > 42:
#     print("Sunny outside,Drink Water")
# elif temperature < 18:
#     print("Its cold,wear a sweater")
# else:
#     print("Tropical heaven")
# print("End of temperature")

# #****************************** ternery operator ********************************
# age = 21
# if age > 18:
#     msg = "Eligible to vote"
# else:
#     msg = "Not Eligible to vote"
# print(msg)

##******************************* Same code written in ternery format *************
# age = 12
# msg = "Eligible" if age > 18 else "Not Eligible"
# print(msg) 

##******************************Logical Operator************************************
#AND
#OR
#NOT

# high_income = False
# good_credit = True
# if high_income and good_credit:
#     print("Eligible for a loan")
# else:
#     print("Not Eligible for a loan")

# msg = "Eligible for a loan " if high_income and good_credit else "Not Eligible for a loan"
# print(msg)

# high_income = False
# good_credit = True
# is_student = False

# if not is_student:
#     msg = "Eligible" if high_income and good_credit else "Not Eligible"
# print(msg)

# high_income = True
# good_credit = False
# is_student = False

# if not is_student:
#     msg = "Eligible for loan" if high_income or good_credit else "Not Eligible"

# print(msg)


# high_income = False
# good_credit = False
# is_student = False

# def set_bools():
#     global high_income
#     high_income = False
#     global good_credit
#     good_credit = False
#     global is_student 
#     is_student=False

# def to_bool(yn):
#     if yn =="y":
#         return True
#     elif yn == "n":
#         return False
#     else:
#         return "nil"

# def userinputs():
#     print("New User Input:")
#     income_input()
#     if (high_income!="nil"):
#         credit_input()
    
#     if(high_income!="nil" and good_credit!="nil"):
#         student_status()

#     if( high_income != "nil" and good_credit!= "nil" and is_student != "nil"):
#         loan_eligibility(high_income,good_credit,is_student)

# def income_input():
#     yn = input("is your income greater than 110k$?[y/n]: ")
#     global high_income 
#     high_income = to_bool(yn.strip().lower())
#     if(high_income=="nil"):
#         print("Invalid input in the income input type[y/n]")

# def credit_input():
#     yn = input("Is your credit score 720 or above?[y/n]: ")
#     global good_credit
#     good_credit = to_bool(yn.strip().lower())  
#     if(credit_input=="nil"):
#         print("Invalid credit input type[y/n]")  

# def student_status():
#     yn = input("Are you a student?[y/n]: ")
#     global is_student
#     is_student = to_bool(yn.strip().lower())
#     if(is_student=="nil"):
#         print("Invalid student status input type[y/n]")

# def loan_eligibility(high_income,good_credit,is_student):
#     if is_student==False:
#         if high_income==True and good_credit==True:
#             print("Fast Track loan processing")
#         elif high_income==False and good_credit == False:
#             print("Not eligible for a loan")
#         elif high_income==False and good_credit==True:
#             print("Eligible under 30K")

#     elif is_student==True:
#         if high_income and good_credit:
#             print("Loan after receiving letter of recommendation")
#         elif high_income and good_credit == False:
#             print("Not eligible for a loan")
#         elif high_income==False and good_credit:
#             print("Eligible under 10K")
    
#     init_yn = input("Enter q to quit or y to continue the enquiry : ")
#     init_yn = to_bool(init_yn)
#     while init_yn== True:
#         set_bools()
        
#         userinputs()
#         if init_yn=="nil":
#             break

# print("*********Welcome to loan sanctioning auto-point , enter the following information*********")
# set_bools()
# userinputs()

#************************************for loops**********************************
# for n in range(1,4):
#     print("Attempt {0} {1}".format(n,n*"."))

# succeful= True
# for n in range(3):
#     print("Attempt {0} {1}".format(n,n*"."))
#     if succeful == True:
#         print("Successful")
#         break
# else:
#     print("Cannot send the mail")


# for x in range(0,6):
#     for y in range(0,4):
#         print("({x},{y})".format(x=x,y=y))


##**********Iterables*********************

# print(type(range(5)))

# for s in "python":
#     print(s)

# for bloom in ["chethi","mantharam","pichakam","chembakam"]:
#     print(bloom)

# command=""  
# while(command.lower() != "quit"):
#     command = input(">")
#     if command.lower() != "quit":
#         print("Echo > {}".format(command))


# while True:
#     command = input(">")
#     if command.lower() == "quit":
#         break
#     else:
#         print("Echo>{}".format(command))


##*****************Kwargs*****key word arguments******************

# def increment(number,by):
#     print("The number {num} is incremented by {by} to {num1}".format(num = number,by = by,num1=number+by))


# print(increment(number=5,by=3))

##***************Default params/required parameters************************
# def increment(number, by=4):
#     return number+by

# incremented_number = increment(80)
# print(incremented_number)

##***************xargs*****************************************************
## type(*nums) = tuple
# def multiply(*nums):
#     n = 1
#     for num in nums:
#         n *= num
#     return n

# print(multiply(1,2,3,4,5))

##******************xxargs*************************************************
## pass in multiple kwargs **user is a dictionary of key-value pair
##{'id': 1, 'name': 'Manu', 'code': 'ad1234'}

# def users(**user):
#     print(user)


# users(id=1,name="Manu",code="ad1234")


##***********************Global*********************************************

# message = "Me a global"

# def email_messaging():
#     global message
#     message = "Me a local"
    
# email_messaging()
# print(message)

# def FizzBuzz(number):
#     if((number % 3 == 0) and (number%5==0)):
#         return "FizzBuzz"
#     elif number % 3 == 0:
#         return "Fizz"
#     elif number % 5 == 0:
#         return "Buzz"
#     else:
#         return number

# print(FizzBuzz(15))
# print(FizzBuzz(9))
# print(FizzBuzz(25))
# print(FizzBuzz(37))

##*******************************calculator***************************
import tkinter as tk
##UI elements require a container/window to place them. 
## To create a root window, enter the following code, and provide a name (<any_name>) for it. 
## You can also rename the window’s title from CALCULATOR to anything you wish.
root = tk.Tk()
## Geometry method that defines the root window size: “width x height”:
root.Geometry("312x324")
## Prevent root window from resizing
root.resizable(0,0)
##Window Title
root.title("Calculator")







