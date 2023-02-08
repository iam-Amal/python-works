
def lst_of_even():
     lst1 =[]
     for i in range(a,b):
          if i % 2 == 0:
               lst1.append(i)

     print(lst1)
a = int(input('enter the first num'))
b = int(input('enter the second num'))
result = lst_of_even()
print(result)