n, s, d = map(int, input().split())
ans = "No"

for _ in range(n):
    x, y = map(int, input().split())
    if s > x and d < y:
        ans = "Yes"

print(ans)
