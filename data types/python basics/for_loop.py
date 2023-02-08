#for i in range(10):
 #   print(i)

#for i in range(2,10):
 #   print(i)
#for i in range(2,18,2):
 #   print(i)
''''
n = int(input('enter the serires of num'))
a,b=0,1
print('fibonacci serires')
print(a)
print(b)
for i in range(2,n+1):
     c=a+b
     print(c)
     a,b=b,c
'''
#to find prime number
''''
num = int(input('enter the num'))
f=0
if num == 1:
    print('not defined')
else:
    for i in range(1,num+1):
        if num%i==0:
            f=f+1
    if f==2:
        print('prime number')
    else:
        print('not prime number')

'''

'''
#else staatement in for loop

for i in 'python':
    print(i)
else:
    print('completed')

'''
'''''
#break statement
l = [10,20,30,50,100,60,70,80]
for i in l:
    print(i)
    if i==100:
        break
'''
'''
#continue statement
l = [10,20,30,50,100,60,70,80]
for i in l:
    if i==100:
        continue
    print(i)
'''
'''
#list
l = [10,20,30,50,]
l1 = [100,60,70,80]
#l.append(l1)
#print(l)
#l.extend(l1)
l.sort()
print(l1)
l.sort(reverse=True)#desecnding a list
print(l)
'''
''''
a = []
x = int(input(('enter num of elements in list:')))
for i in range(x):
    item = int(input('enter the items:'))
    a.append(item)
print(a)
'''


#write a prgrm to print characters from a string that are present at an even index number

str1 = input('enter string')
print('string is',str1)
l = len(str1)
print('character at even index numbers are')
for i in range(0,l,2):
    print(str1[i])





