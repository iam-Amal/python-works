#sum of N numbers

def sum(num):
    if num == 0:
        return 0
    else:
        return num + sum(num-1)

print(sum(5))


#factorial of N numbers

def fact(num):
    if num == 1:
        return 1
    else:
        return num*fact(num-1)

    #5*fact(5-1)=4 fact=4
    #5*fact4(4-1)=3 fact=3
    #5*4*fact3(3-1)=2 fact2
    #5*4*3*fact2(2-1)=1 fact1
    #5*4*3*2*fact1(1-1)=0
    #5*4*2*3*1=120



print(fact(5))