# from csv import writer

# # def add_user(fname,lname):
# #     with open("users.csv","a") as file:
# #         headers = ("First Name","Last Name")
# #         csv_writer = DictWriter(file,fieldnames=headers)
# #         csv_writer.writeheader()
# #         csv_writer.writerow(
# #             {
# #                 "First Name":fname,
# #                 "Last Name": lname

# #             }
# #         )
        
# def add_user(fname,lname):
#     with open("users.csv","a") as file:
#         csv_writer = writer(file)
#         csv_writer.writerow([fname,lname])


        
# add_user("Dwayne", "Johnson")
# add_user("Colt", "Steele")


from csv import  DictReader

def print_users(filename):
    with open(filename) as file:
        csv_reader = DictReader(file)
        names = list(csv_reader)
        for name in names:
            print(name["First Name"]+" "+name["Last Name"])

print_users("users.csv")

