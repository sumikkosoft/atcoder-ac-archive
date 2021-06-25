S = list(input().lower())
x = 0

for i in S:
    if x == 0 and i == "i":
        x += 1
    elif x == 1 and i == "c":
        x += 1
    elif x == 2 and i == "t":
        print("YES")
        exit()

print("NO")
