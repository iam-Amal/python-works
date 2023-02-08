def calculator(func):
    def sum(a,b):
        c = a+b
        return c
    def sub(a,b):
        c = a-b
        return c


@calculator
def divide(a,b):
    c = a/b
    return c


a = print('enter the first num')
b = print('enter the second num')
result =sum(a,b)


