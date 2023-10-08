'''
List items are ordered, changeable, and allow duplicate values.
https://docs.python.org/3/library/stdtypes.html#lists
https://docs.python.org/3/library/stdtypes.html#typesseq-common
https://docs.python.org/3/library/stdtypes.html#typesseq-mutable
'''

# can be of any data type
myList = ["abc", 34, True, 40, "male"]
print(type(myList))
print(len(myList))
print(myList[0])   # first item
print(myList[-1])  # last item
print(myList[2:4])  # range of indexes (start included, end not included)
print(myList[:4])  # from start
print(myList[2:])  # till the end
print(myList[-4:-1])  # 3 items
print(myList[-1:-4])  # empty
print(40 in myList)  # Exist? True
myList[3] = 42
print(myList)
myList[1:2] = [True, False]  # replace 1 item by 2, increase the size
print(myList)
myList[1:4] = [3]  # replace 3 items by 1, decrease the size
print(myList)
myList[1:4] = [3]  # replace 3 items by 1, decrease the size
print(myList)
myList.insert(1, "watermelon")  # insert befor index 1
print(myList)
myList.append("orange")  # insert at the end
print(myList)

# list construtor
fruits = list(("apple", "banana", "cherry"))
print(fruits)  # note the double round-brackets

iterable = list("apple")  # iterable item
print(iterable)

print(iterable * 3)  # multiply the content
print(myList + fruits)  # concatenation
myList.extend(fruits)  # concatenation
print(myList)
iterable += fruits  # concatenation
print(iterable)
myList.remove("banana")
print(myList)
print(myList.pop())  # pop at end
print(myList.pop(0))  # pop at index 0
print(myList)
del myList[0]
print(myList)
myList.clear()
print(myList)
del myList  # the list is not defined anymore

myList = fruits
myCopy1 = myList.copy()  # copy
myCopy2 = list(myList)  # copy
print(myCopy1 == myCopy2)  # True
print(myCopy1 is myCopy2)  # False

[print(x) for x in fruits]  # list comprehension

print("\nList comprehension with conditional")
myList = [x for x in fruits if "a" in x]
print(myList)

print("\nTernary operator in list comprehension")
myList = [x if x != "banana" else "Orange" for x in fruits]
print(myList)

print("\nSorting")
print(myList, 'original')
myList.reverse()
print(myList, 'reversed')
print(sorted(myList, reverse=True), 'with return')
myList.sort(reverse=True)
print(myList, 'descending')
myList.sort()
print(myList, 'sorted')
myList.sort(key=str.lower)
print(myList, 'case insensitive')

print("min: ", min(myList))
print("max: ", max(myList))
print("{} occurs {} times.".format("cherry", myList.count("cherry")))  # count
print("index: ", myList.index("cherry"))
