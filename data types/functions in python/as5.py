def addition(a,b):
    def calaulate():
        c = a + b
        return c
    return calaulate()+5

num1 = int(input('enter the first number'))
num2 = int(input('enter the second number'))
result = addition(num1,num2)
print(result)
