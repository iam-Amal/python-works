str1 = 'Luminar'
print(str1)
dict1 = {}
for index in range(1,len(str1)+1):
    dict1.setdefault(index,str1[index-1])
#    print(index,str1[index-1])
print(dict1)