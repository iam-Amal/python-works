lst1=[]
def creat():
    num = int(input('enter the elements in list :'))
    for i in range(num):
        item=int(input('enter item:'))
        lst1.append(item)
    print(lst1)

def search():
    item=int(input(('enter the item :')))
    if item in lst1:
        print('item is in the list')
    else:
        print('not in the list')

def remove():
    item=int(input('enter the item to remove :'))
    if item in lst1:
        lst1.remove(item)
    else:
        print('item not found!')
    print(lst1)

def replace():
    item=int(input('enter the item to replace :'))
    new_item=int(input('enter the new item to be replaced :'))
    for i in range(len(lst1)):
        if lst1[i]==item:
            lst1[i]=new_item
    print(lst1)

while True:
    options=int(input('1-creat\n2-search\n3-remove\n4-replace\nEnter your choice :'))
    if options==1:
        creat()
    elif options==2:
        search()
    elif options==3:
        remove()
    elif options==4:
        replace()
    else:
        break




#creat()
#search()
##remove()
#replace()





