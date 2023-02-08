smpl_data = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
setof_uvalues = set()
for i in smpl_data:
   # print(i)
    for values in i.values():
        print(values)
        setof_uvalues.add(values)
print(setof_uvalues)