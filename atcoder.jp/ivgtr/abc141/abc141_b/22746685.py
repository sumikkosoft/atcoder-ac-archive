N = list(input())

for i in range(len(N)):
    if i % 2:
        if N[i] not in ["L", "U", "D"]:
            print("No")
            exit()
    else:
        if N[i] not in ["R", "U", "D"]:
            print("No")
            exit()

print("Yes")
