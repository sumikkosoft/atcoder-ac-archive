n = int(input())
ans = 0

for i in range(1, 7):
    if 2 ** i <= n:
        ans = i


print(2 ** ans)
