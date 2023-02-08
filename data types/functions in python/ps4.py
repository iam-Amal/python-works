def prime(num):
    count = 0
    i = 2
    while(i<=num//2):
        if(num % i == 0):
            count = count + 1
            break
        i = i + 1
    if (count == 0 and num != 1):
        print(' is prime')
    else:
        print('is not prime')


number = int(input('enter the number'))
prime(number)