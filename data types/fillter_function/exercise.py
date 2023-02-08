ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)

for x in adults:
  print(x)



#using lambda functiom

age = [22,12,25,16,18]
adult = filter(lambda a : if < 18,age)
print(list(adult))
