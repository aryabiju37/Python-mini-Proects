def find_and_replace(file_name,find,replace):
    with open(file_name,"r+") as file:
        content = file.read()

        new_content = content.replace(find,replace)
        file.seek(0)
        file.write(new_content)



find_and_replace("alice.txt","Alice","Colt")
