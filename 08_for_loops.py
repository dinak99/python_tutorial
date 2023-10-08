print("\nLoop through Sequence Types")
fruits = ["apple", "banana", "cherry"]
for i in fruits:
    print(i)

print("\nLoop through strings")
for i in "apple":
    print(i)

print("\nLoop through ranges")
for i in range(3):
    print(i)

print("\nLoop through specific ranges")
for i in range(1, 4):
    print(i)

print("\nLoop through ranges stepping by 2")
for i in range(-2, 5, 2):
    print(i)

print("\nBreak and continue")
for i in range(10):
    if i == 3:
        continue
    elif i == 6:
        break

    print(i)

print("\nElse")
for i in range(3):
    print(i)
else:
    print(f"last index: {i}")  # won't work in presence of break

print("\nPass and explicit list")
for i in [0, 1, 2]:
    pass  # use pass for an empty loop

print("\nList Comprehension")
[print(x) for x in fruits]
