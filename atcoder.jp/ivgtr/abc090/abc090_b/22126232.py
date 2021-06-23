a, b = map(int, input().split())
ans = 0

for i in range(a, b + 1):
    x = str(i)
    if x == x[::-1]:
        ans += 1

print(ans)
