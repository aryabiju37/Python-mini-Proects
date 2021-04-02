from functools import  wraps

def only_ints(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        tuple_lst = [x for x in args if type(x)!= int]
        if tuple_lst != []:
            return "Please only invoke integers"
        else:
            return fn(*args,**kwargs)
    return wrapper

@only_ints
def add(x,y):
    return x + y


print(add(1,2))
print(add("1","2")) 


        