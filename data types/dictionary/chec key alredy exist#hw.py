dict1 = {1:"a",2:"b",3:"c"}
key = int(input("enter the key"))
if dict1.get(key):
    print("you have the key")
else:
    print("key dose not exist")