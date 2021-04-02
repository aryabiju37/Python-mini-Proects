with open("story.txt") as f:
    data = f.read()

haha.txt is automatically created when used like the below:
with open("haha.txt","w") as file:
    file.write("Haha"*1000)

with open("haiku.txt","w") as haiku:
    haiku.write("Here's one more haiku\n")
    haiku.write("What about the older one? \n")
    haiku.write("Let's go checkout!!")

modes in file handling
with open("haiku.txt","a") as haiku:
    haiku.seek(0)
    haiku.write(":D \n")    


