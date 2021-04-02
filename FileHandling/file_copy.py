def copy(original,copied):
    with open(original,"r") as file:
        content = file.read()

    with open(copied,"w") as cfile:
        cfile.write(content)

copy("haiku.txt","copies.txt")