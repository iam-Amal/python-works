"""
str1 = 'restart'

char = str1[0]
print(char)
lenght = len(str1)
print(lenght)
str1 = str1.replace(char,'$')
print(str1)
str1 = char+str1[1:]
print(str1)
"""
'''
str1 = input('enter the string')
if str1.istitle():
  print('all lettres are capital')
else:
  print('all leters are not capital')
'''
'''''
str1 = input('enter the sentens')
words = str1.split()
for word in words:
  if word[0].isupper():
    print(f"{word} begins with capitel letter")
  else:
    print(f"{word} dose not begins with capital leter")
'''''
'''''
str1 = 'Hi am Amal'
w = str1.split()
for i in w:
  #print(i)
  if i[0].isupper():
    print(f'{i } word is printed in caps')
  else:
    print(f'{i} word is not cap')
'''''

