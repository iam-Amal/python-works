print('Arguments (args)/positional args\n************************')
def my_function(msg1,msg2):
    print(msg1 + ' ' + msg2)
my_function('hello','how are you')
my_function('whats','your name')


print('Arbitry arguments\n*************************')
def my_func(*names):
    print('hi',names,'hello')
my_func('amal','jack')
my_func('jack')


print('Keyword arguments\n*************************')
def func(name1,name2,name3):
    print('last names  '+name2)
func('amal',name3='jin',name2='jerrin')



print('Aribatry keyword argument(**kwargs)\n************************************')
