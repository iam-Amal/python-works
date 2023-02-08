# print(dir(list))
# print(dir(dict))

lst = [
    [1, 34],
    [40, 5],
    [5, 70]
]
# print all number>50
'''
for ls in lst:  # ls=[1,34]
    for num in ls:
        if num > 50:
            print(num)
'''
# using list comprihension
'''
numbers = [num for ls in lst for num in ls]#to print list
print(numbers)
'''
# list comprihension using conditions
'''
numbers = [num for ls in lst for num in ls if num > 50]
print(numbers)
'''
# to find max value using max function
'''
print(max([num for ls in lst for num in ls]))
'''
# print [5,70] pair
''''
max_num=[num for ls in lst for num in ls]
print(max_num)
max_pair = [ls for ls in lst if max_num in ls]
print(max_pair)
'''

# HW
lst1 = [1, 2, 3, 4]
output = 7  # (4,3)
# find the pair of output 7 using one loop
'''
for i in range(len(lst1)):
#    print(i)

    for j in range(i+1,len(lst1)):
         print(j)
#        if lst1[i]+lst1[j]==7:
 #           print((lst1[i],lst1[j]))

'''

'''
seen = set()
for num in lst1:
    if 7 - num in seen:
        print((num, 7-num))
    seen.add(num)

'''


