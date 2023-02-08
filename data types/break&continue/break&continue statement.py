for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("finished")

for j in range(6):
    if j ==4:
        continue
    print(j)

#while loop
a = 1
while(i<=10):
    if a == 4:
        break
    print(i)
    i = i+1



#multiplication table using while loop

b = 1
num = int(input("enter the number"))
while b<=10:
    print("%dX%d=%d\n"%(num*b))
    b=b+1