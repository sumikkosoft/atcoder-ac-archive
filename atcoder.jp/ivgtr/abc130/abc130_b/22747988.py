N, L = map(int, input().split())
x = list(map(int, input().split()))
tmp = 0
ans = 1
for i in range(N):
    tmp += x[i]
    if tmp <= L:
        ans += 1

print(ans)
