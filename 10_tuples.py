# Tuple items are ordered, unchangeable, and allow duplicate values.

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

thistuple = ("apple",)  # one item tuple, remember the comma
print(type(thistuple))

# tuple construtor
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)  # note the double round-brackets

iterable = tuple('apple')  # iterable item
print(iterable)

# Tuples are unchangeable, or immutable as it also is called. But there is a workaround:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# unpacking
fruits = ("apple", "banana", "cherry")  # also works for lists, try with []
(green, yellow, red) = fruits  # also works for lists, try with []
print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits  # groups the rest on the variable with asterisc
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
# groups the rest on the variable with asterisc, except the last one
(green, *tropic, red) = fruits
print(tropic)
