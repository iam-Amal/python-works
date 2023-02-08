#Python function that accepts different values as parameters and returns a list


def func(*args):#variable length arg

    return list(args)
lst1 = func(1,2,3,4,'amal')
print(lst1)