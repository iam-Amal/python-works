tple = (1,2,3,4,5,"me",8.5)
print(tple)
print(tuple(tple))
print(len(tple))
print(tple[0])
print(tple[-1])
print(tple[1:2])
print(tple[0:4])
print(tple[::-1])
print(tple[:-5])
print(tple[-4:-1])
print()
print('to update tuple')
#to update tuple
a = list(tple)
a[1] = "amal"
tple = tuple(a)
print(tple)
print('to append a value')
a.append(77)
tple = tuple(a)
print(tple)
a.append('heloo')
tple = tuple(a)
print(tple)
print('add a tuple to the existing one')
tple1 = ('hello','hi',9,9.5)
tple += tple1
print(tple)
print('to remove an item from tuple')
x = list(tple)
x.remove('hello')
tple = tuple(x)
print(tple)
print('del function dose not support')
#print('del function')
#tpl2 = (1,2,3,4,5,6)
#del tpl2
#print(tpl2)

print('unpacking a tuple')
fruits = ('apple','mango')

print('looop in tuple\n***********')
for i in tple1:
    print(i)
print('while loop\n*******')





new_tple = ("amal",[1,2,3],('hi',7,6))
print(new_tple[0])
print(new_tple[1][2])
print(new_tple[2][1])
print('if the elements is mutable dataype like list,its items can be changed')
new_tple[1][1] = 4
print(new_tple)
print(all(new_tple))