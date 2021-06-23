n = int(input())
h = list(map(int, input().split()))

ans = 0
for i in range(1, 101):
    c = 0
    for j in h:
        if j >= i:
            c = 1
        else:
            ans += c
            c = 0
    else:
        if c == 1:
            ans += 1

print(ans)
