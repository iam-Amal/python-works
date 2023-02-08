def fact(x):
    if x==1:
        return 1
    else:
        return x*fact(x-1)



f=fact(5)
print(f)

#5*4!-120
#4*3!-24
#3*2!-6
#2*1!-2