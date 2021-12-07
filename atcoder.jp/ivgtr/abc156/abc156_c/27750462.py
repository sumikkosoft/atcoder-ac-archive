N = int(input())
X = list(map(int, input().split()))

ans = float("inf")

for i in range(100):
    tmp = 0
    for j in range(N):
        tmp += (X[j] - i) ** 2
    ans = min(ans, tmp)

print(ans)
