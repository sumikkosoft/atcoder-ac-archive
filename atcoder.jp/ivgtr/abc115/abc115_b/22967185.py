N = int(input())

ans = 0
tmp = 0
for i in range(N):
    x = int(input())
    ans += x
    tmp = max(tmp, x)

ans -= int(tmp / 2)

print(ans)
