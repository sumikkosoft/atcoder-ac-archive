N = int(input())
H = list(map(int, input().split()))

tmp = float("inf")

for h in reversed(H):
    if tmp >= h:
        tmp = h
    elif tmp >= h - 1:
        tmp = h - 1
    else:
        print("No")
        exit()


print("Yes")
