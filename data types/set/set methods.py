#print('set is immutable\nunorderd\nunindexed\nduplicatesare not allowed')
#print('set items are unchangeble,but you can remove items and add items')

A = {2,4,6,8,10}
B = {5,4,3,2,1}
print('union:',A | B)
print('intersection=',A & B)
print('defference =',A - B)
print('symmetric diff',A ^ B)


print('add a list of elements to a set')

sampl_set = {0,1,2,3}
lst1 = [4,5,6]
sampl_set.update(lst1)
print(sampl_set)

print('get only unique items from two sets')
set1 = {10,20,30,40,50}
set2 = {30,40,50,60,70}
print(set1.union(set2))
print('check if two sets have any elements in comon.'
      'display the comon elements')
st1 = {10,20,30,40,50}
st2 = {30,40,50,60,70}
if st1.isdisjoint(st2):
    print('two sets have no items in common')
else:
    print('two sets have items in comon')
    print(st1.intersection(st2))
print('reomove items from set1 that are not common both')
st1.intersection_update(st2)
print(st1)