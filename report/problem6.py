for i in range(0, 5):
    for j in range(i, 4):
        print(" ", end="")
    for j in range(i, -1, -1):
        print("*", end="")
    print()