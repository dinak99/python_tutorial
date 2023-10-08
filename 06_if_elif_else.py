a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

if b > a:
    pass  # use pass for an empty IF

if (a != 0 or b != 0) and b > a:
    pass  # use of AND/OR

# if a > b: print("a is greater than b") # VSCode formatter always move to the next line
print("A") if a > b else print("B")  # Ternary Operator
# print("A") if a > b else print("=") if a == b else print("B")  # nested Ternary Operator
