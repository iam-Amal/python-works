smpldata = [{'item':'item1','amount':400},{'item':'item2','amount':300},{'item':'item1','amount':750}]
#print(smpledata)
#newdict = {}
#list1 = []
#for i in smpldata:
#    #print(i)
#    p = list(i.values())
#    #print(p)
#    list1.append(p[0])
#    list1.append(p[1])
#print(list1)
#for i in range(0,len(list1),2):
#    if list1[i] in newdict:
#        rep = list1[i]
#        print(rep)


list1 = {}
for i in smpldata:

  if i['item'] not in list1:
      list1[i['item']]=i['amount']
  else:
      list1[i['item']]+=i['amount']
print(list1)