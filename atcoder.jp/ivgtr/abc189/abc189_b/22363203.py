n, x = map(int, input().split())
x *= 100
ans = 1

for _ in range(n):
    v, p = map(int, input().split())
    x -= v * p
    if x >= 0:
        ans += 1


if x >= 0:
    print(-1)
else:
    print(ans)
