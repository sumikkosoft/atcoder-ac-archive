x, y = map(int, input().split())

if x > y:
    y += 3
    if x < y:
        print("Yes")
    else:
        print("No")
else:
    x += 3
    if x > y:
        print("Yes")
    else:
        print("No")
