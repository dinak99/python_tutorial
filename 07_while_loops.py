i = 0
while i < 4:
    print(i)
    i += 1

print("\nSecond loop: break and continue")
i = 0
while i < 10:
    i += 1

    if i == 3:
        continue
    elif i == 6:
        break

    print(i)

print("\nThird loop: else")
i = 0
while i < 4:
    print(i)
    i += 1
else:
    print(f"last index: {i}")  # won't work in presence of break
