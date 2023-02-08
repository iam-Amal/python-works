def sum(a,b):
    print('sum = ',a+b)
def sub(a,b):
    print('sub =',a-b)
def mul(a,b):
    print('mul =',a*b)
def div(a,b):
    print('div =',a/b)
a = int(input('enter the first num'))
b = int(input('enter the second num'))
choice = int(input('1.addition\n'
                   '2.subtraction\n'
                   '3.multiplication\n'
                   '4.division\n'
                   'enter your choice :'))
if choice==1:
    sum(a,b)
elif choice==2:
    sub(a,b)
elif choice==3:
    mul(a,b)
elif choice==4:
    div(a,b)
else:
    print('not available')