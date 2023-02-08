 ''''
def colour(*args):
    print(args[0])
    for i in args:
        print(i)

colour('red','white','pink')
'''
#arbitary argument
''''
def colours(x,*args):
    print('normal argument',x)
    for i in args:
        print(i)

colours('red','white','pink','black')
'''
'''
#keywrod argument
#key=value

def stud(st1,st2,st3):
    print('first:',st1)
    print('second:', st2)
    print('third:', st3)
stud('amal','ani','arun')
stud(st1='ani',st2='amal',st3='arun')



def student(**kwargs):
    for i ,j in kwargs.items():
        print('%s=%s'%(i,j))

student(st2='Anu',st1='amal',st3='ani')
'''
'''
def stu(x,*args,**kwargs):
    print('simple arg:',x)
    for j in args:
        print('arbitart arg:',j)
    for i,j in kwargs.items():
        print('%s=%s'%(i,j))
stu('amal','varun','sini',st2='anu',st1='arun',st3='ani')
'''
'''
#default parameter

def display(country='india'):
    print('i am from',country)
display()
display('kunnamkulam')

#list
def dis(ls):
    for i in ls:
        print(i)

dis([10,20,30,40])
'''

lst1=[]
def creat():
    num = int(input('enter the elements in list :'))
    for i in range(num):
        item=int(input('enter item:'))
        lst1.append(item)
    print(lst1)

def search():
    item=int(input(('enter the item :')))
    if item in lst1:
        print('item is in the list')
    else:
        print('not in the list')

def remove():
    item=int(input('enter the item to remove :'))
    if item in lst1:
        lst1.remove(item)
    else:
        print('item not found!')
    print(lst1)

def replace():
    item=int(input('enter the item to replace :'))
    new_item=int(input('enter the new item to be replaced :'))
    for i in range(len(lst1)):
        if lst1[i]==item:
            lst1[i]=new_item
    print(lst1)

while True:
    options=int(input('1-crea\n2-search\n3-remove\n4-replace\nEnter your choice :'))
    if options==1:
        creat()
    elif options==2:
        search()
    elif options==3:
        remove()
    elif options==4:
        replace()
    else:
        break




#creat()
#search()
##remove()
#replace()





