# 1.Encapsulation-wraping up of data and and function in to single unit
#eg:class

# 2.inheritence-to accure the properties of one class to another class is called inheritence
#types of inheritence are
# a.Single inheritence
# b.multilevel inheritence
# c. hierarchical inheritence
# d. hibrid inheritence

# 3.polymorphism that is one in many forms
#twoo type of polymorphism thats are
#1.compile time
#eg:Function overloading
#2.Run time
#eg:function overriding
#Function overloading means one class how more than one function with same function name and different signature(number,order and type of parameters)
#Function overriding means difernt class have diferent function with same function name and same signatures

# 4.Abstraction--is to reperesent the essential feaures with out representing explaination or background details
#main advantage is data hiding
#a class that consists of one or more abstract method is called abstract class
#absract class can be inherited by the sub class and abstract method gets its definiton in sub class
#pyton provides 'abc module' to use the abstraction in python prgrm
#we need to import this abc module which provides base for definiton Abstract Base Class(ABC)
#the ABC works by decorating methods of the base class as abstract
# we use @abstractmethod decorator to define an abstract method
#if we dont provide the definiton the method is automaticaly become the abstract method

# 5.constructor
#these are the member function of a class which will automaticaly exicuted when an object of a class is created
#constructers do not have return value
#we can define a constructer by using '__init__()'
#there are 2 types of constructers
#a.non parametrised constructer
#b.parameterised cunstuctos





#1.inheritence
'''
#a.sinlge inheritence
use=code reusabilty


class A:
    def displayA(self):
        print('Base call method')
class B(A):
    def displayB(self):
        print('derive class method')
obj=B()
obj.displayA()
obj.displayB()


#sample programe
class A:
    def read(self):
        self.x=int(input('enter the firs value:'))
        self.y=int(input('enter the second value:'))
class B(A):
    def sum(self):
        print('sum is:',self.x+self.y)

obj=B()
obj.read()
obj.sum()
'''

'''
#b.multilevel inheritence

class A:
    def read(self):
        self.x=int(input('enterthe first num:'))
        self.y=int(input('enter the second num'))
class B(A):
    def sum(self):
        self.s=self.x+self.y
        print('sum is:',self.s)
class C(B):
    def avg(self):
        print('avarage is',self.s/2)

obj=C()
obj.read()
obj.sum()
obj.avg()
'''

'''
#c.hierarchical inheritence


class A:
    def read(self):
        self.x=int(input('enter the firs num:'))
        self.y=int(input('enter the second num:'))
class B(A):
    def sum(self):
        self.s=self.x+self.y
        print('sum is:',self.s)
class C(B):
    def avg(self):
        self.a=(self.x+self.y)/2
        print('avarage is:',self.a)
class D(C):
    def product(self):
        self.p=self.x*self.y
        print('product is:',self.p)

obj1=B()
obj1.read()
obj1.sum()

obj2=C()
obj2.read()
obj2.avg()

obj3=D()
obj3.read()
obj3.product()
'''

#d.Multiple inheritence
'''
class A:
    def employees(self):
        self.name=input('enter your name:')
        self.age=int(input('enter your age:'))
        self.address=input('enter your adress')
class B:
    def salary(self):
        self.amount=int(input('enter your salary'))
        self.bank=input('enter your bank name:')
class C(A,B):
    def details(self):
        #print('Name is:',self.name,'\nAge is:',self.age,'\nAdd is:',self.address,'\nsalary is:',self.salary(),'\nBank is:',self.bank)
        print('{}:{},{}:{},{}:{},{}:{},{}:{}'.format('name is:',self.name,'Age is:',self.age,'Address is:',self.address,'salary is:',self.amount,'bank name:',self.bank))


obj=C()
obj.employees()
obj.salary()
obj.details()
'''
#2.polymorphism
'''
#function overloading

class A:
    def display(self,name=None):
        if name is None:
            print('hello')
        else:
            print('hello'+name)

obj=A()
obj.display()
obj.display('amal')
'''


#function overriding
'''
class rectangle:
    def Area(self,l,b):
        print('area of rectangle:',l*b)

class square(rectangle):
    def Area(self,l,b):
        print('area of sqaure :',l*b)

obj=square()
obj.Area(10,20)
'''
#homework for tomorow(super function)


# 3.Abstraction method
'''
from abc import ABC,abstractmethod
#abstract class
class polygon(ABC):
    @abstractmethod
    def sides(self):
        pass
    def display(self):
        print('non abstract method')

class triangle(polygon):
        def sides(self):
         print('trianlge has 3 sides')

t=triangle()
t.sides()
t.display()

'''
# 5.constructers

#a.Nonparameterized constructor
'''
class A:
    def __init__(self):
        print('Non parameterized constructer')
ob=A()
'''

#b.Parametrized construtor
'''
class A:
    def __init__(self,name):
        self.na=name

    def display(self):
        print('my name is ',self.na)

obj=A('Amal')
obj.display()
'''

#homework(regular expresion tutorial)

#homework for tomorow(super function)
''''
class Name:
    def __init__(self):
        print('my name is Amal')

class Name2(Name):
    def __init__(self):
        print('his name is shyam')
        #Name.__init__(self)
        super().__init__()

obj=Name2()

'''