# print total num of phones
from products.models import mobiles

#print(len(mobiles))  # output=5products

# print all mobile names
'''
for mob in mobiles:
    #print(mob['name'])
    #print(mob.get('name'))
'''
# using list comprehension
'''
mobile_name = [mob.get("name") for mob in mobiles]
print(mobile_name)
'''
# print all samsung mobiles
'''
samsung = [mob for mob in mobiles if mob["brand"] == "samsung"]
print(samsung)
samsung_mob=[mob.get("name") for mob in mobiles if mob.get("brand")=="samsung]
'''
# print all costly mobiles

#rate = [mob for mob in mobiles if mob['price'] > 30000]
#print(rate)
print(max([mob.get("price") for mob in mobiles if mob.get("price")]))

    # sorted
'''
x=sorted(mobiles, key=lambda mob: mob.get("price"), reverse=True)
print(x)
'''