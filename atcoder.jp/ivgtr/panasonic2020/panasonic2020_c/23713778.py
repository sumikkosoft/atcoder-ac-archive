A, B, C = map(int, input().split())

if 4 * A * B < (C - A - B) ** 2 and A + B < C:
    print("Yes")
else:
    print("No")
