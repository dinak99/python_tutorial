# A dictionary is a collection which is ordered (after v3.7), changeable and do not allow duplicates.
# https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2022,  # duplicate values will overwrite existing values
    "colors": ["red", "white", "blue"],
    123: 'number',
}
print(thisdict)
print(thisdict["year"])
print(thisdict.get("year"))
print(thisdict["colors"])
print(thisdict[123])
copy = dict(thisdict)  # constructor

thisdict["letter"] = 'c'  # creates a new key
thisdict.update({"wheels": 4})  # add a new set of pairs
thisdict.update({"wheels": 4})  # add a new set of pairs
[('brand', 'Ford'), ('model', 'Mustang'), ('year', 2022), ('colors', [
    'red', 'white', 'blue']), (123, 'number'), ('letter', 'c'), ('wheels', 4)]
print(thisdict.keys())
print(thisdict.values())

items = thisdict.items()
print(type(thisdict))
print(type(items))
print(items)

print("model" in thisdict)  # key exist? True
print(2022 in thisdict.values())  # value exist? True

del thisdict["model"]
thisdict.pop("brand")
print(thisdict.popitem()[0])  # removes the last inserted item
# (in versions before 3.7, a random item is removed instead)

print(thisdict)

print("\nKeys:")
for x in thisdict:  # shortcut to print all keys
    print(x, sep=' , ', end=' ', flush=True)
print("")  # newline

print("\nKeys (iterator):")
for x in iter(thisdict):
    print(x, sep=' , ', end=' ', flush=True)
print("")  # newline

print("\nItems:")
for x, y in thisdict.items():  # print all items
    print(x, y)

myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
print(myfamily)  # nested dictionary

array = ('first', 'second', 'third')
map = dict.fromkeys(array, 0)
# for x in array:
#     map[x] = 0  # initializes
print(map)

map = {array[i]: i+1 for i in range(len(array))}  # dict_comprehension
map['fourth'] = 2
map['zourth'] = 2
print(map)

print(sorted(map.items()))  # sort by key
print(sorted(map.items(), key=lambda item: int(item[1])*-1))  # sort by value
print(sorted(map.items(), key=lambda item: (
    item[1], item[0])))  # sort by value
