limit = int(input("enter the limit ="))
num1 = 0
num2 = 1
sum = 0
while num1 <=limit:
    print(num1)
    sum = num1+num2
    num1 = num2
    num2 = sum