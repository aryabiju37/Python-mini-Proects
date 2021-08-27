# def sentencemaker(phrase):
#     questions = ("how","why","where","when","who","what")
#     if phrase.startswith(questions):
#         return " {}?".format(phrase.capitalize())
#     else:
#         return "    {}".format(phrase.capitalize())

# input_str=[]
# while True:
    
#     user_says = input("Say Something : ")
   
    
#     if user_says == "\end":
#         print(" ".join(input_str))
#         break
#     else:
#         input_str.append(sentencemaker(user_says))
#         continue

# listgeneral = [12,3,4,5,'noone',323,9,'arya']
# def listmanipulation(listgeneral):
#     for lst in listgeneral:
#         if type(lst)==str:
#             listgeneral[listgeneral.index(lst)]=0
#     return listgeneral

# print(listmanipulation(listgeneral))

# mymanipulatedlist = [0 if type(x)==str else x for x in listgeneral]
# print(mymanipulatedlist)
# lst=[1,4,6]
# lst=[1.7,3.5,4.5]
# def summation(lst):
#     sum_l=0
#     for l in lst:
#         sum_l += l
#     return sum_l

# print(summation(lst))

# for i in lst:
#     print(i)
# sums = 0       
# [sums:= sums+x for x in lst]
# print(sums)
# def concatstr(str1,str2):
#     return str1+str2

# print(concatstr("Arta","sreedhar"))
# def foo(*args):
#     return sum(args)/len(args)

# print(foo(1,25,34,56))
# def foo(*args):
#     lst = []
#     for strings in args:
#         lst.append(strings.upper()) 
#     return sorted(lst)


# print(foo("arya","biju","aries"))

# file = open("fruits.txt")
# print(file.read())
# print(file.read())    
# #concept of cursor,try reading files only once
# file = open("fruits.txt")
# contents = file.read()
# print(contents)
# print(contents)

#closing files with "with" context manager
# with open("fruits.txt") as myfile:
#     content = myfile.read()

# print(content)

# with open("vegetables.txt","w") as myfile:
#     myfile.write("Onions\nCucumber\n")
#     myfile.write("Tomatoes")
# path1 = "/home/arya/Documents/pyprojs/files/fruits.txt"
# def foo(str1,path1):
#     with open(path1,"r") as myfile:
#         contents=myfile.read()
#         if str1 in contents:
#             return contents.count(str1)
#         else:
#             return 0

# print(foo("pear",path1))

# reader = open("files/fruits.txt","r")
# contents = reader.read()
# reader.close()
# writer = open("file.txt","w")
# writer.write(contents)
# writer.close()

#appending to files
# with open("files/fruits.txt","a+") as myfile:
#     myfile.write("\nMangoes")
#     myfile.seek(0)
#     content = myfile.read()
# print(content)


##************ Find and replace something wrong with the code, duplicate insertion**********

# def foo(txtfind,txtReplace):
#     with open("files/fruits.txt","a+") as myfile1:
#         myfile1.seek(0)
#         contents=myfile1.read()
#         if txtfind in contents:
#             myfile1.seek(0)
#             myfile1.write(contents.replace(txtfind,txtReplace)) 
        
# foo("pear","berries")


