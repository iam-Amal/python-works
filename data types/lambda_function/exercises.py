#WAP to creat a function that takes one argemt and that arguement will be multiplied wiht an unknown given number


def mul(num):
    return lambda a : a * num
x = mul(2)
print(x(5))


#WAP to fillter a list of intigers using lambda

a = [1,2,3,4,5,6,7,8,9,10]
even_num = list(filter(lambda a : a%2 == 0,a))
print(even_num)

odd_num = list(filter(lambda a : a%2 != 0,a))
print(odd_num)



#lambda with if else conditons

value = lambda a,b : a if(a>b) else b
print(value(1,3))


