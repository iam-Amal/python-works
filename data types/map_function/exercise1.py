def func(a,b):
    return a +b
x = map(func,('apple','orange'),('banana','pinaple'))
print(list(x))



fruits = 'apple','orange','banana','pineapple'
c = map(lambda a : a.upper(),fruits)
print(list(c))



