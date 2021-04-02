def get_multiples(num=1,count=10):
    for i in range(1,count+1):

        if i < count+1:
            yield i*num
        else:
            pass
# def get_multiples(num=1, count=10):
#     next_num = num
#     while count > 0:
#         yield next_num
#         count -= 1
#         next_num += num

sevens = get_multiples(7,15)
print(next(sevens))
print(next(sevens))
print(next(sevens))
print(next(sevens))
print(next(sevens))
print(next(sevens))
print(next(sevens))
print(next(sevens))
print(next(sevens))
print(next(sevens))
print(next(sevens))
print(next(sevens))
print(next(sevens))
print(next(sevens))
print(next(sevens))


