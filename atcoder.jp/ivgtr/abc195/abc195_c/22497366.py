N = int(input())
tmp = (len(str(N)) - 1) // 3
ans = 0
for i in range(1, tmp + 1):
    ans += N - (1000 ** i - 1)

print(ans)
