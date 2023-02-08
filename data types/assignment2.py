mark1 = int(input("physics mark ="))
mark2 = int(input("chemistry ="))
mark3 = int(input("biology ="))
mark4 = int(input("maths ="))
mark5 = int(input("computer ="))
per = (mark1+mark2+mark3+mark4+mark5)*100/500
print(per,"%")
if per >=90:
    print("A grade")
elif per >=80:
    print("B grade")
elif per >=70:
    print("C grade")
elif per >=60:
    print("D grade")
elif per >=40:
    print("E grade")
else:
    print("FAIL")