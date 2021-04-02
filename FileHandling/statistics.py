def stats(filename):
    with open(filename) as file:
        content = file.read()
    # print(content)
    lines = content.split("\n")
    
    # print(len(lines))
    wrds=""
    for i in range(len(lines)-1):
        wrds +=lines[i]+" "
    
    wrdsplit = wrds.split()    
    # print(len(wrdsplit))
    charcount=0
    for wrd in wrdsplit:
        charcount += len(wrd)
    # print(charcount)
    
    return {"lines":len(lines),
    "words":len(wrdsplit),
    "characters":charcount}


print(stats("haiku.txt"))
    

    