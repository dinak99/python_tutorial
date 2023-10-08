###############################################################################################################################
# Random number
from sys import maxsize, exit
import random
print(random.randrange(1, 100))
max = maxsize
min = (maxsize - 1) * -1
print(max)
print(min)
exit()
'''
Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
'''

###############################################################################################################################
# Get the type
x = 5
print(type(x))
print(isinstance(x, int))

###############################################################################################################################
# Setting the data type
x = "Hello World"  # str
x = 20  # int
x = 20.5  # float
x = 1j  # complex
x = ["apple", "banana", "cherry"]  # list
x = ("apple", "banana", "cherry")  # tuple
x = range(6)  # range
x = {"name": "John", "age": 36}  # dict
x = {"apple", "banana", "cherry"}  # set
x = frozenset({"apple", "banana", "cherry"})  # frozenset
x = True  # bool
x = b"Hello"  # bytes
x = bytearray(5)  # bytearray
x = memoryview(bytes(5))  # memoryview
x = None  # NoneType
print(type(x))

###############################################################################################################################
# Setting the specific data type
x = str("Hello World")
x = int(20)
x = float(20.5)
x = complex(1j)
x = list(("apple", "banana", "cherry"))
x = tuple(("apple", "banana", "cherry"))
x = range(6)
x = dict(name="John", age=36)
x = set(("apple", "banana", "cherry"))
x = frozenset(("apple", "banana", "cherry"))
x = bool(5)
x = bytes(5)
x = bytearray(5)
x = memoryview(bytes(5))
x = None
print(type(x))

###############################################################################################################################
# int has unlimited length
x = 1
y = 35_656_222_554_887_711
z = -3_255_522
print(type(x))
print(type(y))
print(type(z))

###############################################################################################################################
# float in scientifc notation
x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))

###############################################################################################################################
# Strings
str = "Oneline \
string"
print(str)
str = '''Multiline
string'''
print(str)
print(str[1])  # strings are arrays

for c in str:  # loop through the letters in the word
    print(c)

str = ' banana'
print(len(str))             # string length
print("nana" in str)        # contains()
print("nana" not in str)    # not contains()
print(str.upper())
print(str.lower())
print(str.strip())          # removes whitespaces
print(str.replace("a", "X"))
print(str.split("a"))
# all string methods: https://docs.python.org/3/library/stdtypes.html#string-methods

a = "Hello"
b = "World"
c = a + " " + b
print(c)  # concatenation

quantity = 3
item = "banana"
print(f"I want {quantity} pieces of item {item}.")  # printf
print("I want {} pieces of item {}.".format(quantity, item))  # printf
print("I want {1} pieces of item {0}.".format(quantity, item))  # with indexes
print(item, quantity, sep=' , ', end=' ', flush=True)
print("")  # newline

###############################################################################################################################
# Operators
print(5 / 3)    # regular division
print(5//3)     # Floor division (DIV)
print(5 % 3)    # Modulus (MOD)
print(5**3)     # Exponentiation

x = 4
x += 1
print(x)  # increment: x++
print(not (x > 3 and x < 10))  # False: operators and/or/not

###############################################################################################################################
# Identity operator (consider memory location)
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)  # True: same object
print(x is y)  # False: only same content
print(x == y)  # True: same content

###############################################################################################################################
# Membership operator
x = ["apple", "banana"]
print("banana" in x)        # True
print("banana" not in x)    # False
