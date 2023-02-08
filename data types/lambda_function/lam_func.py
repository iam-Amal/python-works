x = lambda a : a+10
print(x(3))
y = lambda c,d : c + d


print(y(10,5))

def my_func(n):
    return lambda a : a * n
mul = my_func(2)
print(mul(10))
