import time

gen_start = time.time()
print(sum(n for n in range(100000000)))
gen_stop = time.time() - gen_start

lst_start = time.time()
print(sum([n for n in range(10000000000)]))
lst_stop = time.time() - lst_start

print("generator took {} time".format(gen_stop))
print("list comprehension took {} ".format(lst_stop))

# n =(n for n in range(1,10))
# ## n is a generator object
# next(n)


