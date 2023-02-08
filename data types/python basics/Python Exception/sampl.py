try:
    a=int(input('enter the first num:'))
    b=int(input('enter the second num:'))
    c=a/b
    print('output:',c)

except Exception as ex:
    print(ex)

#except ZeroDivisionError as er:
    #print(er)

#except ValueError as er:
#    print(er)