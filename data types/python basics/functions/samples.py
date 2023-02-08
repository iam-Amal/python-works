#function
#oops-programs are based on class and object
#class-class is the way to bind functions and its related data
#object-instance of a class or runtime entity of  a class
#function-repeated group of statements or function for perticular task


#function has two parts-1-function definition and 2-function calling
#Return value-we can pass only one value from function definition to  function calling is called return value
#function parameters-we can pass more than one value from function calling to function definition


'''
#return value eg:
def sum():
    a,b=10,20
    c=a+b
    return c
    #print(c)

print('sum is',sum())
'''

#function prarameter eg:
def sum(x,y):
    a=x+y
    return a

print('sum is:',sum(12,20))


#wap to find factorial of a number using function with return type and function parameter


def fact(num):



#different type of parameter
#1-simple,2-arbitary,3-keyword,4-default parameter,5-list
#simple argument

''''
def colour(x,y,z):
colour('red','white','pink')
print(colour())
'''

def colour(*args):
    print(args[0])
    for i in args:
        print(i)

colour('red','white','pink')