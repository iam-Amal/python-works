#file handling is an important of web application
#python has severel functions for 'creating','reading','updating' and 'deleting'files
#the key function of working with a file is the 'open()' function
#open() function take 2 parameters that is filename and mod
#differtn methods(mods) for openig a file are
#1. "r"--Read-default value open a file for reading ,error if the file dose not exist
#2. "a"--Append-Open file for appending.Creates a file if it dose not exist
#3. "w"--Write-Open a file for writing ,creat file if dose not exist
#4. 'x'--Creat-creat the specified file,return error if file alredy exists


# 1. 'r'
'''
f=open('test1','r')
#print(f.read()) ---#for reading the whole file
print(f.readline())
print(f.readline()) #for reading line by line
print(f.readline())
'''

'''
#using forloop
f=open('test1','r')
for i in f:
    print(i)
f.close()#use close() function after opened a file
'''
# 2.'a'
#Append method is used to append data in to the end of the file
'''
f=open('test1','a')
f.write('ihihihihihihihhi')
f.close()
'''
'''
f=open('test1','r')
print(f.read())
f.close()
'''


# 3.'w'
'''
f=open('test1','w')
f.write('python is oopS')
f.close()

f=open('test1','r')
for i in f:
    print(i)
'''

#seek() method sets the current file position in a file stream
#it also returns the new position
#syntax--file.seek(offsetvalue)
'''
f=open('test1','r')
f.seek(8)
print(f.readline())
f.close()
'''

#tell() method returns the position of the file
#syntax--fileobject.tell()
'''
f=open('test1','r')
f.readline()
pos=f.tell()
f.close()
print('position is:',pos)
'''

#write a programe to read a file line by line and store it in to a list
#using readlines() method
'''
def file_read(file_name):
    with open(file_name) as f:
        output_list=f.readlines()
    print(output_list)

file_read('test1')
'''

#copy data from one file to another file
'''
from shutil import copyfile
copyfile('test1','test2')
'''

'''
str1='cat rat mat cat pat rat cat sat cat sat'

print(str1)
lst=str1.split(' ')
print(lst)
dict1={}
for i in lst:
    if i in dict1:
        dict1[i]=dict1[i]+1
    else:
        dict1[i]=1

print(dict1)

'''
#homework--do this with file handling

f=open('test 3','r')
d={}
for i in f:
    var=i.split(' ')
    for j in var:
        if j not in d:
            d[j]=1
        else:
             d[j]+=1

print(d)



