def copy_and_reverse(ofile,cfile):
    with open(ofile) as file:
        content = file.read()
        r_content = content[::-1]

    with open(cfile,"w") as copy:
        copy.write(r_content) 


copy_and_reverse("copies.txt","revcopy.txt")