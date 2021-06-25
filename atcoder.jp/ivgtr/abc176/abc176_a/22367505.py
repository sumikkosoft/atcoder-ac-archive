n, x, t = map(int, input().split())

ans = n // x * t
if n % x:
    ans += t

print(ans)
