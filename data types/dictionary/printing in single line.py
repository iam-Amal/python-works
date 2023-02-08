dict1 = {"name":"amal","age":"22","dob":"1998"}
print(dict1)
print(type(dict1))
print(dict1["name"])
print(dict1.get("age"))
print(dict1.values())
print(dict1.keys())
print(dict1.items())#to get as tuple
dict1["age"] =20#change values
print(dict1)
dict1.update({"dob":"2000","name":"me"})#change values,can add multiple
print(dict1)
dict1["place"] = "kottakkal"
print(dict1)
dict1.pop("age")
print(dict1)
dict1.popitem()#remove last item in dictionary
print(dict1)
del dict1["name"]
print(dict1)
dict2 = {"name":"amal","age":"22","dob":"1998"}
print(dict2)
dict2.clear()
print(dict2)
dict3 = {"name":"amal","age":"22","dob":"1998"}

for i in dict3.keys():
     print(i)
dict3.copy()
print(dict3)
