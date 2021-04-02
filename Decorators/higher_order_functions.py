def sum(num,func):
    total = 0
    for x in range(1,num+1):
        total += func(x)
    return total


def square(x):
    return x**2

def cube(x):
    return x**3

print(sum(3,square))