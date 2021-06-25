N = int(input())
ans = 0

for i in range(N // 2 + 1):
    for j in range(N // 2 + 1):
        if i ** j <= N:
            ans = max(ans, i ** j)

print(ans)
