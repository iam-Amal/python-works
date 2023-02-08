'''
row = int(input(("enter the row :")))
for i in range(1,row+1):
    for j in range(i):
        print(j+1,end=" ")
    print()
'''
num=int(input('enter the num:'))
n1=0
n2=1
sum=0
while n1<=num:
    sum=n1+n2
    print(n1)
    n1=n2
    n2=sum