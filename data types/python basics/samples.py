"""""
num1,num2=int(input('entr the first num1')),int(input('enter the second num2'))
num1,num2=num2,num1
print('num1 :',num1)
print('num2 :',num2)
"""
'''''
#to check wether a num is postive negstive or 0

a = int(input('enter the num'))
if a > 0:
    print('positive')
elif a < 0:
    print('negative')
else:
    print('0')
    
  '''''

''''
#largest of 3 num using nusted if
a = int(input('enter the num'))
b = int(input('enter the num'))
c = int(input('enter the num'))
if a > b:
    if a > c:
        print('a is largest',a)
    else:
        print('c is largest',c)
elif b>c:
    print('b is largesst',b)
else:
    print('c is largest',c)

'''

#reverse of a number using while loop
a = 123
rev = 0
while a>0:
    r = a%10
    rev = rev*10+r
    product = product*r
    sum = sum*r
    a = a//10
print('reverse is :',rev)
print()







