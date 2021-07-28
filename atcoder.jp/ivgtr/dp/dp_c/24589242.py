N = int(input())
X = [list(map(int, input().split())) for _ in range(N)]
ABC = 3
DP = [[0 for _ in range(ABC)] for _ in range(N)]
DP[0] = X[0]


for i in range(1, N):
    for j in range(ABC):
        for k in range(ABC):
            if j != k:
                DP[i][j] = max(DP[i][j], DP[i - 1][k] + X[i][j])

print(max(DP[-1]))
