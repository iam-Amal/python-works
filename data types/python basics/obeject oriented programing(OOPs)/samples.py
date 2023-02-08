#syntax

class Employee:
    x=50
    def display(self):
        print('sample function')
obj=Employee()
obj.display()
print('value of x:',obj.x)

#without self arguement
'''
class Emp():
    x=100
    def display():
        print('with out self parameter')

obj=Emp
obj.display()
'''
'''
class Arithametic():
    def math_function(self):
        print('answers')
    def sum(self,a,b):
        print('sum is',a+b)
    def product(self,a,b):
        print('product is',a*b)
        
obj=Arithametic()
obj.sum(10,20)
obj.product(2,2)
'''

'''
class Arithemetic:
    def read(self,a,b):
        self.x=a
        self.y=b
    def sum(self):
        print('sum is:',self.x+self.y)
    def product(p):
        print('product is:',p.x*p.y)


obj=Arithemetic()
obj.read(10,20)
obj.sum()
obj.product()

'''
'''
class arithemetic():
    def read(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
        print('sum is:',self.a+self.b)


obj=arithemetic()
obj.read(10,5)
obj.sum()

'''
#to find fact of a number using class with function arguments and return value

class Factorial():
    def fact(self,a):
        f=1
        for i in range(1,a+1):
            f=f*i
        return f
obj=Factorial()
f=obj.fact(5)
print('factorial is:',f)


class Fact():
    def fact(self,x):
        if x==1:
            return 1
        else:
            return x*self.fact(x-1)

f=obj.fact(5)
print(f)


