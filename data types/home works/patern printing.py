num = int(input("enter the number ="))
for i in range(num-2):
    for s in range(i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
    