from csv import DictReader

def find_user(fname,lname):
    with open("users.csv") as file:
        csv_reader = DictReader(file)
        users = list(csv_reader)
        
        res=[]            
        res = [user["First Name"]==fname and user["Last Name"]==lname for user in users]
        if True in res:
            return res.index(True)
            #dlfkpodsjfskdnk
        return "{first} {last} not found.".format(first=fname,last=lname)
            

        
        
        
            
        
                
        


         


            
            


print(find_user("Alan","Turing"))
print(find_user("Alan","jakobson"))