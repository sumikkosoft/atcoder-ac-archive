a = int(input())

for i1 in range(9):
    for i2 in range(9):
        if (i1 + 1) * (i2 + 1) == a:
            print("Yes")
            exit()

print("No")
