n, d, h = map(int, input().split())
ans = 0
for _ in range(n):
    di, hi = map(int, input().split())
    x = d - di
    y = h - hi
    z = h - (d / x * y)
    if z <= 0:
        z = 0
    ans = max(ans, z)

print(ans)
