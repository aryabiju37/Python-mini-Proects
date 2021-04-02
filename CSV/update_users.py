from csv import DictReader,DictWriter,writer
def update_users(fname,lname,nfname,nlname):
    with open("users.csv","r") as file:
        csv_reader = DictReader(file)
        users = list(csv_reader)
        res=[]
        update_count=0
        res = [user["First Name"]==fname and user["Last Name"]==lname for user in users]
        if True in res:
            user_index = res.index(True)
            users[user_index]["First Name"]=nfname
            users[user_index]["Last Name"] = nlname
            print(users)
            with open("users.csv","w") as wfile:
                headers = ["First Name","Last Name"]
                csv_writer = DictWriter(wfile,fieldnames=headers)
                csv_writer.writeheader()
                for user in users:
                    csv_writer.writerow(
                        {
                            "First Name":user["First Name"],
                            "Last Name":user["Last Name"]

                        }
                    )
               
                update_count += 1
            print("Users Updated: {}".format(update_count))
        else:
            print("Users Updated: {}".format(update_count))
                
                

print(update_users("Alan","Turing","ratan","tata"))

