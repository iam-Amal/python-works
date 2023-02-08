str1 = 'kanakambaran'
print(type(str1))
tple = tuple(str1)
print(tple)
print('list to tuple')
list1 = [1,2,3,4,5]
print(type(list1))
tuple = tuple(list1)
print(tuple)
print('repeated items from tuple')
tple2 = (1,2,2,2,2,8,6)
print(tple2.count(2))


tupl = (1,2,4,3,5,6,7,7,8)
print(len(tupl))
print(all(tupl))
print(max(tupl))
print(min(tupl))
print(sorted(tupl))


print('Enumerate function')
names = ['hi','hello','hoo']
ages = [24,50,18]
for i,(name,age) in enumerate(zip(names,ages)):
     print(i,names,ages)



