from random import choice

def make_laugh():
    def laugh_types():
        type_laugh = choice(("HAHAHAA","LOLOLOL","TROLOLOLOL","HEHEHEHEHE"))
        return type_laugh

    return laugh_types

laugh = make_laugh()
print(laugh())


# If you assign a function reference to a variable, then that variable will point to a function 
# and you can add parentheses to call/execute it like a normal function.
#  Functions in Python are also objects and they can be assigned to variables.