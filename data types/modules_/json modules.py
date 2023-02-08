




import json

x = '{"Name":"Amal","Age":"23","Course":"Python"}'
print(type(x))
#json to python
y = json.loads(x)
print(type(y))