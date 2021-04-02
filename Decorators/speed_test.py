from time import time
from functools import wraps

def speed_test(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        start_time = time()
        result = fn(*args,**kwargs)
        time_elapsed = time() - start_time
        print(f"Time Elapsed: {time_elapsed}")
        return result
    return wrapper

@speed_test
def sum_nums():
    return sum(x for x in range(1000000000))

print(sum_nums())