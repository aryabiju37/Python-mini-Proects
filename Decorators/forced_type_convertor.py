from functools import wraps
def type_converter(*types):
    def func(fn):
        @wraps(fn)
        def wrapper(*args,**kwargs):
            converted_args=[]
            for (t,a) in zip(types,args):
                converted_args.append(t(a))
            return fn(*converted_args,**kwargs)
        return wrapper
    return func

@type_converter(str,int)
def repeat_msg(msg,time):
    for time in range(time):
        print(msg)

@type_converter(int,int)
def divide(a,b):
    print(a/b)

print(divide("10","2"))

print(repeat_msg("Hello",3))
