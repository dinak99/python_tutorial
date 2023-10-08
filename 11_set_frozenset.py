# Set items are unordered, unindexed, and do not allow duplicate values.

# https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
"""
There are currently two built-in set types, set and frozenset.
The set type is mutable — the contents can be changed using methods like add() and remove().
The frozenset type is immutable and hashable — its contents cannot be altered after it is created.
"""

thisset = {"apple", "banana", "cherry"}
print(thisset)  # the items will appear in a random order.

fs = frozenset(thisset)
print(fs)

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)  # duplicate values will be ignored

# set construtor
thisset = set(("apple", "banana", "cherry"))
print(thisset)  # note the double round-brackets

thisset.add("orange")  # add item
print(thisset)

tropical = {"pineapple", "mango", "papaya", "banana"}
# it can be any iterable object (tuples, lists, dictionaries etc.).
print(tropical)

# Union: join and exclude any duplicate items
union = thisset.union(tropical)  # calc and returns
# thisset.update(tropical)  # calc and replaces
print(union, "union")

# Intersection: keep ONLY the duplicates
intesection = thisset.intersection(tropical)  # calc and returns
# thisset.intersection_update(tropical)  # calc and replaces
print(intesection, "intesection")

# Difference: only the elements that are NOT present in the other
difference = thisset.difference(tropical)  # calc and returns
# thisset.difference_update(tropical)  # calc and replaces
print(difference, "difference")

# Symmetric difference: only the elements that are NOT present in both sets
symmDiff = thisset.symmetric_difference(tropical)  # calc and returns
# thisset.symmetric_difference_update(tropical)  # calc and replaces
print(symmDiff, "symmDiff")

thisset.remove("banana")
print(thisset)  # if it not exist, remove() will raise an error.

thisset.discard("banana")
print(thisset)  # if it not exist, remove() will NOT raise an error.
