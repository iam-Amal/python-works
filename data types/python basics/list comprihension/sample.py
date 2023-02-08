#list comprehension provides an easy way to apply opereations on a list
#it crates a new list in which each elements is the result of applying a given operation in a list
#synatx:list[expression-'for' item 'in' list 'if' conditon]
'''
lst=[x+3 for x in [1,2,3,4]]
print(lst)
'''
'''
#to find even numbers in 1-25
lst1=[i for i in range(1,26) if i%2==0]
print(lst1)
'''

#to retur vowels from a string
'''
str1='hello world'
v=[i for i in str1 if i in ['a','e','i','o','u']]
print(v)
'''
#to print firs letter of each words in a string
'''
str1 = 'hi how are you'
a=str1.split()
print(list(a))
first_letter=[i[0] for i in a]
print(first_letter)
'''
#to find a perticular letter in a list
'''
colours=['red','white','green','pink']
letter=[i for i in colours if 'e' in i]
print(letter)
'''
#to print a list without a word in the given list
'''
colours=['red','white','green','pink']
new_lst=[i for i in colours if i!= 'green']
print(new_lst)
'''

#to apply build in methods in list comprihension
'''
colours=['red','white','green','pink']
new_list=[i.upper() for i in colours]
print(new_list)
'''

#if else conditons in list comprihension
colours=['red','white','green','pink']
print('old lsit:',colours)
new_list=[i if i!='pink' else 'blue' for i in colours]
print('updated list:',new_list)
