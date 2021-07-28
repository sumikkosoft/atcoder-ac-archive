N, W = map(int, input().split())
X = [[]]

for _ in range(N):
    X.append(list(map(int, input().split())))

ans = 0
DP = [[0 for _ in range(W + 1)] for _ in range(N + 1)]


for i in range(1, N + 1):
    for weight in range(1, W + 1):
        if weight - X[i][0] >= 0:
            DP[i][weight] = max(
                DP[i - 1][weight - X[i][0]] + X[i][1], DP[i - 1][weight]
            )
        else:
            DP[i][weight] = DP[i - 1][weight]

print(DP[-1][-1])
