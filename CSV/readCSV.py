# from csv import reader
# with open("fighters.csv") as file:
#     csv_reader = reader(file)
    #csv_reader is an iterbale
#     #with header of csv
#     for row in csv_reader:
#         #each row is a list
#         print("{} is from {}".format(row[0],row[1]))


# from csv import reader
# with open("fighters.csv") as file:
#     csv_reader = reader(file)
#     #with header
#     next(csv_reader)
#     for row in csv_reader:
#         #each row is a list
#         print("{} is from {}".format(row[0],row[1]))


#csv_reader is an iterable which we can use to access the 
#data to print without for loop you can just convert it into a list
# from csv import reader
# with open("fighters.csv") as file:
#     csv_reader = reader(file)
#     lst_reader = list(csv_reader)
#     print(lst_reader)



#***********using dictreader***********
from csv import DictReader

with open("fighters.csv") as file:
    dict_reader = DictReader(file)
    for row in dict_reader:
        print(row)
        print(row["Name"])
