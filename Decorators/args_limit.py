def count_args(*args,**kwargs):
    type_lst = [x for x in args if type(x)==int]
    print(type_lst)
    print(type_lst.__contains__(int))


print(count_args(1,2,3,4,5,6,"Arya"))