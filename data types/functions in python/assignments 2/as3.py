#.Assign a different name to function and call it through the new name

def addition():
    a = int(input('enter the num1: '))
    b = int(input('enter the num2: '))
    c = a + b
    print(c)
sum = addition
result = sum()
