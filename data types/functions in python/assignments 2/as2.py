"""""
.Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included).
"""""

def values_of_square():
    lst1 = []
    for i in range(a,b):
            lst1.append(i**2)
    print(lst1)
def list_enterd():
    lst2 = []
    for i in range(a,b):
        lst2.append(i)
    print(lst2)


a = int(input('entert the first value :'))
b = int(input('enter the last value :'))
original_list = list_enterd()
print(original_list)
square_of_list = values_of_square()
print(square_of_list)