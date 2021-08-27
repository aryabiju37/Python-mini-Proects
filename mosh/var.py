# student_count = 1000
# course_name = "python programming"
# rating = 4.99
# is_enrolled = True

# #********************strings***************************************************
# course = "python programming"
# print(" The length of the course is : {} ".format(len(course)))
# print(" Slice of the course is : {} ".format(course[0:3]))
# print(" The last letter of the course is : {} ".format(course[-1]))
# print(" The different way to slice the course is : {} ".format(course[:3]))

# #*****************************Escape sequences*********************************
# # \"
# # \'
# # \\
# # \n 
# # \t

# print("\" Python Programming \" ")

# #*******************************String methods************************************
# course = " python programming"
# print("Titling the course {}".format(course.title()))
# print("Upper of the  course {}".format(course.upper()))
# print("Lower of the course {}".format(course.lower()))
# print("Find sequence of the course {}".format(course.find("pro")))
# print("replacing the course {}".format(course.replace("p","j")))
# print("pro" in course)
# print("swift" not in course)

# #***********************Numbers******************************************************
# print("Addn: {}".format(10+3))
# print("Subtraction: {}".format(10-3))
# print("Mul: {} ".format(10*3))
# print("Div: {}".format(10/3))
# print("Floor Div {}".format(10//3))
# print("Power: {}".format(10**3))
# print("modulus div : {}".format(10%3))

# #**************************math module*************************************************
# import math 
# print(abs(2.99))
# print(abs(-2.99))
# print(math.ceil(2.45))

# #********************************Type conversion****************************************
# x = int(input("Enter the value for var x: "))
# print("x :{}".format(x))

# #*******************************Falsy types in python ***********************************
# # ""
# # 0
# # None 
# # False
# # All the remaining types are True

# print(bool(""))
# print(bool(0))
# print(bool(None))
# print(bool(False))
# print(bool("False"))

##*****************************Comparison OPerator******************************************
# print("10>3        :  {}".format(10>3))
# print("10>=3       :  {}".format(10>=3))
# print("20<10       :  {}".format(20<10))
# print("20>=3       :  {}".format(20>=3))
# print("10!=\"10\"  :  {}".format(10!=10))
# print("10==10      :  {}".format(10==10))

##*******************Comparison for strings**************************************************
# print("bag > apple: {}".format("bag">"apple"))
# ## string sort () ==> order of asc , therefore bag>apple == True
# print("BAG == bag: {}".format("BAG" == "bag"))