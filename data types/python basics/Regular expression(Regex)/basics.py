#is used to check if a string contains the specified search pattern
#python has a build in package called 're' which can be work with regular expression
#used in pyhton for serverside validation
#methods in Regex:
#1.find all()
#it return a list containing all matches
'''
import re
str1='rose is a beautyful and colerful flower'
s=re.findall('ful',str1)
print(s)
#if there is no matches it will return an empty list
s=re.findall('full',str1)
print(s)

str2='cat,mat,rat,sat'
a=re.findall('[cs]',str2)
print(a)
a=re.findall('[sc]at',str2)
print(a)

# [^]--except that single characters eg:[^sc]
str3='cat,mat,rat'
b=re.findall('[^mc]',str3)
print(b)

#\d--read only digit
#{}--number of digit
str3='cat,mat,rat,9998,999,13465'
c=re.findall('\d{3}',str3)
print(c)

str3='cat,mat,rat,9998,999,13465'
c=re.findall('\d{1,4}',str3)
print(c)

# r--read
#\b--word boundry
str3='cat,mat,rat,9998 9999 1346'
c=re.findall(r'\b\d{4}\b',str3)
print(c)
'''

#2.search()
#it returns a match object ith there is a match anywhere in the string
'''
# \s--match any whitespace,including spaces,tabs,line break
s1='class will start at 10am'
s=re.search('\s',s1)
print(s)
print(s.start())
s=re.search('\d',s1)
print(s.start())
#if we search not matching object None will return
s=re.search('python',s1)
print(s)


#^--start of a line.
# .--match any single character
# *--to match zero or more occurence of the preceding character
# $-to match the ending of line

s=re.search('^class.*10am$',s1)
if s:
    print('find')
else:
    print('not find')
'''

# 3.split()
'''
s1='class will start at 10am'
s=re.split(' ',s1)
print(s)
s=re.split('a',s1)
print(s)
s=re.split(' ',s1,3)
print(s)
'''

#4.fullmatch()
'''
str1='python is a language'
a=re.fullmatch(str1,'python is a language')
print(a)
'''

#5.sub()
'''
#it replaces one or many mathces with a string
input='rose and jasmine are flowers'
a=re.sub(' ','*',input)
print(a)
a=re.sub(' ','*',input,2)
print(a)
'''


#Email validation
'''
# Make a regular expression
# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


# Define a function for
# for validating an Email
def check(email):

    # pass the regular expression
    # and the string into the fullmatch() method
    if (re.fullmatch(regex, email)):
        print("Valid Email")

    else:
        print("Invalid Email")

a='amal3247@gamil.com'
check(a)
b='amal.gamil.com'
check(b)
'''


#tomorow hmwrk
#phone numbervalidation



# Python program to check if
# given mobile number is valid
'''
import re


def isValid(s):
    # 1) Begins with 0 or 91
    # 2) Then contains 6,7 or 8 or 9.
    # 3) Then contains 9 digits
    Pattern = re.compile("(0|91)?[6-9][0-9]{9}")
    return Pattern.match(s)


# Driver Code
s =(input('enter the mobile number:'))
if (isValid(s)):
    print("Valid Number")
else:
    print("Invalid Number")
'''


#passwordvalidation
#Should have at least one number.
#Should have at least one uppercase and one lowercase character.
#Should have at least one special symbol.
#Should be between 6 to 20 characters long.

# importing re library
import re


def main():
    passwd = input('enter the password:')
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"

    # compiling regex
    pat = re.compile(reg)

    # searching regex
    mat = re.search(pat, passwd)

    # validating conditions
    if mat:
        print("Password is valid.")
    else:
        print("Password invalid !!")


#Driver Code
if __name__ == '__main__':
    main()


