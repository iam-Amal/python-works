#Define a function that accepts a number and returns whether the number is even or odd.

def num(a):
    if a%2 == 0:
        return 'Even'
    else:
        return 'odd'

a = int(input('enter a number'))
result = num(a)
print(result)

