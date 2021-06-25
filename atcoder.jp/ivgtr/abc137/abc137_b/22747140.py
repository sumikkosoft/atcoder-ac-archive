K, X = map(int, input().split())
mx = 1000000
mi = -1000000

ans = []

for i in range(X, X + K):
    if i <= mx:
        ans.append(i)

for i in range(X - K + 1, X):
    if i >= mi:
        ans.append(i)

ans.sort()

print(*ans)
