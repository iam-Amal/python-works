#reverse a number using while loop
n=123
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10

print(rev)

'''
num=456
rev=0
while num>0:
    r=num%10
    #print(r)
    rev=rev*10+r
    #print(rev)
    num=num//10
    print(num)

print(rev)
'''
num=326
rev=0
while num>0:
    r=num%10
    rev=rev*10+r
    num=num//10
print(rev)


'''
num=int(input('enter the num'))
i=1
lst1=[]
while len(lst1)<num:
    lst1.append(i)
    i=i+1
print(lst1)
'''


a=int(input('enter the num'))
i=1
total=0
while i<=a:
    total=total+i
    i=i+1
    avg=total/a
print(avg)