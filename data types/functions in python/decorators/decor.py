def make_pretty(func):

    def inner():
        print('i got decoratod')
        func()
    return inner

@make_pretty
def ordinery():
    print('i am ordinery')


ordinery()




def upper_decor(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper()

def hello_name():
    return 'hello'

f = upper_decor(hello_name)
print(f)


#using '@' symbol for decarator


def upper_decor(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@upper_decor
def hello_name():
    return 'hello'
print(hello_name())
