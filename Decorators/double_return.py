from functools import wraps
import copy

def double_return(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        val=fn(*args,**kwargs)
        lst=[]
        lst.extend([val,copy.copy(val)])
        return lst
    return wrapper

# @double_return
# def greet(name):
#     return "Hi I'm {}".format(name)

@double_return
def add(x,y):
    return x+y

print(add(2,3))
        
        
        