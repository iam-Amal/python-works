def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)

n = int(input('enter a num'))
result = factorial(n)
print(result)