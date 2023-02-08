age = int(input("enter the age :"))
if age <= 18:
    print("not eligible")
else:
    print("eligible")


num = int(input("enter a number :"))
if (num % 2) ==0:
    print(num,"is even")
else:
    print(num,"is odd")


print("enter 3 numbers \n")
num1 = int(input())
num2 = int(input())
num3  = int(input())
if num1 >= num2 and num1 >= num3:
    print(num1,"greater")
elif num1 >= num3:
    print(num2,"is greater")
else:
    print(num3,"greater")
