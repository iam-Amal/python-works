print('max of three num')
def max_of_three(a,b,c):
    if a>b and a>c:
        print('largest =',a)
    elif b>a and b>c:
        print('largest',b)
    else:
        print('largest =',c)

max_of_three(2,4,6)
max_of_three(6,4,2)
max_of_three(4,6,2)


print('sum of list')
def sum_list(lst1):
    sum = 0
    for i in lst1:
        #print(i)
        sum = sum+i
    print(sum)


sum_list([1,2,3,4])
sum_list([1,2,3,4,5])



print('multi list')
def multi_list(lst):
    total = 1
    for i in lst:
        total = total*i
    print(total)

multi_list([1,2,3,4])
