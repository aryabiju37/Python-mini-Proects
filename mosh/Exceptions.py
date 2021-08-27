##Exception Handling in python
# try:
#     age = int(input("Enter your age : "))

# except ValueError as ex:
#     print("Enter a valid age in numbers")
#     print(ex)
#     print(type(ex))
# else:
#     print("No exceptions were thrown! ")

"""catching all exceptoins, always type the generic expressions at the end after catching 
all the other exceptions
"""
# try:
#     age = int(input("PLease enter your age in numbers: "))
#     xfactor = 10/age

# except Exception as ex:
#     print("Please eneter a valid age that is a number and not zero")

##catching exceptions by types

# try:
#     age = int(input("please enter your age: "))
#     xfactor=10/age
# except ValueError:
#     print("ENter a valid age in numbers")

# except ZeroDivisionError:
#     print("You just divided by zero")

# else:
#     print("No exceptions caught")


"""
file,network conn, sql conn must always be closed in the finally block*

"""
# try:
#     file = open("conditional.py")
#     age = int(input("please enter your age: "))
#     xfactor=10/age
# except ValueError:
#     print("ENter a valid age in numbers")

# except ZeroDivisionError:
#     print("You just divided by zero")

# else:
#     print("No exceptions caught")

# finally:
#     file.close()

"""
an object havinig .__Enter__ and .__Exit__ methods support context management protocol and 
python automatically releases the resources file,sql,network connection objs while used with a
"with" statement, multiple file open is also supported by "with", hence we need not release these resources in the finally block
"""
# try:
#     with open("Exceptions.py") as file,open("conditional.py") as file1 :
#         file.readline()
#     age = int(input("Enter a valid age: "))
#     xfactor = 10/age

# except (ValueError,ZeroDivisionError):
#     print("Enter a valid age")
# else:
#     print("No exception caught")

