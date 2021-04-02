from functools import wraps
#see it this way: define a wrapper and put it inside a function
def ensure_first_arg(val):
    def fn_outside_wrapper(fn):
        @wraps(fn)
        def wrapper(*args,**kwargs):
            if args and args[0] != val:
                return "First arg needs to be {}".format(val)
            return fn(*args,**kwargs)
        return wrapper
    return fn_outside_wrapper
    
@ensure_first_arg("burrito")
def fav_foods(*foods):
    print(foods)

print(fav_foods("burrito","banana"))
print(fav_foods("banana","grapes"))

    