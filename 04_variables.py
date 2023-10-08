###############################################################################################################################
# No need of type. Can change type
x = 4        # x is of type int
x = "Sally"  # x is now of type str
print(x)

###############################################################################################################################
# Casting
x = str(3)
y = int(3)
z = float(3)
k = float("3")
s = str(3.0)
print(x)
print(y)
print(z)
print(k)
print(s)

###############################################################################################################################
# Get the type
x = 5
y = "John"
print(type(x))
print(type(y))
print(isinstance(x, int))  # True

###############################################################################################################################
# Single or Double Quotes?
x = "John"
# is the same as
y = 'John'
print(x)
print(y)

###############################################################################################################################
# Set all at once
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

###############################################################################################################################
# Unpack a collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

###############################################################################################################################
# output
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = "John"
print(x, y)  # don't try: 5 + "John"

###############################################################################################################################
# booleans
# https://docs.python.org/3/reference/expressions.html#comparisons
print(3 > 2 > 1)
print(1 < 2 < 3)  # Comparisons can be chained arbitrarily
print(1 < 2 > 3)
print(1 <= 2 >= 2)

###############################################################################################################################
# input

# Python 3.6
username = input("Enter username: ")
print("Username is: " + username)

# Python 2.7
# username = raw_input("Enter username: ")
# print("Username is: " + username)
