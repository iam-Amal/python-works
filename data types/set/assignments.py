print('1.	Remove empty strings from a list of strings')
str1 = ["jhon"," ","Jack","Emma"," ","Jins","Lina"]
print(str1)
while (" " in str1):
    str1.remove(" ")
print(str1)

print('2.Write a python code to remove all the repeating letters.from a each words of a given sentence.')
smpl_str1 = 'Let’s google the pineapple'
st1 = smpl_str1.split(' ')
#print(st1)
st2 =[]
#print(st2)
for i in st1:
    #print(i)
    l = ""
    for j in i:
        #print(j)
        if j in l:
            continue
        else:
            l = l+j
            #print(l)
    st2.append(l)
    #print(st2)
print(' '.join(st2))


print('3.	Replace each special symbol with # in the following string')
str2 = '/*Jon is @developer & musician!!'
str2.replace('/*','#')
restr2 = str2.replace('/*','#').replace('@','#').replace('&','#').replace('!','#')
print(restr2)

print('4.Reverse a list in Python')
lst1 = [100, 200, 300, 400, 500]
relst = lst1[::-1]
print(relst)

print('5.	Extend nested list by adding the sublist')
lst01 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
ex_lst = ["h","i","j"]
lst01[2][1][2].extend(ex_lst)
print(lst01)
