from json import load


with open("db.json", "r",encoding="UTF-8") as f:
    data = load(f)

print(len(data))

# movie_name=[movie.get("title")for movie in data]
# print(movie_name)

'''
print([movies.get("title")for movies in data if movies.get("year")=="2002"])
'''

# Hw
# list movie names with gener=comedy

from json import load

with open("db.json", "r") as f:
    data = load(f)
#print([movies.get("title") for movies in data if "Comedy" in movies.get("genres")])

# output=> one year=num of movies

#year="1984"
#year="2012"
#print([movies.get("title")for movies in data if movies.get("year")==year])
mc={}
for m in data:
    year=m.get("year")
    if year in mc:
        mc[year]+=1
    else:
        mc[year]=1
print(mc)
#which is the year that released most num of movie
print(max(mc,key=lambda k:m.get(k)))
#print(max(mc.items(),key=lambda t:t[1]))


# lengthi movie
'''
print(max(data,key=lambda m: int(m.get("runtime"))))

shortest_movie=min(data,key=lambda m:int(m.get("runtime")))
print(shortest_movie)
'''