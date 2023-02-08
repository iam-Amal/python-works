#Define a function that accepts 2 values and return its sum, subtraction and multiplication


def val(a,b):
    sum = a + b
    subtraction = a - b
    multiplication = a * b
    return sum,subtraction,multiplication
a = int(input('enter 1st num'))
b = int(input('2nd num'))
result = val(a,b)
print(result)

