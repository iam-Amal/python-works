#lambda function is a small anonimous function
#it can take any number of arguiments but can only have one expression
'''
def sum(a,b):
    return a+b
print(sum(10,20))
'''
#syntax:lambda arguments:expression
'''
add=lambda a,b:a+b
print(add(2,3))
'''
#largest of 2 numbers using lambda
'''
largest=lambda a,b:a if (a>b) else b
print(largest(55,6))
'''
#filter,map,reduce methods in lambda function

#1.filter
lst1=[10,2,3,4,50,77,11]
lst2=list(filter(lambda x:x%2==0,lst1))
print(lst2)

#2.map

lst1=[10,2,3,4,50,77,11]
lst2=list(map(lambda x:x*2,lst1))
print(lst2)

#3.reduce

from functools import reduce
lst1=[1,2,3,4,5]
product=reduce(lambda x,y:x*y,lst1)
print(product)
#what are the difference btw lambda function and user defined function?(google it)


