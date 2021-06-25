N, K = map(int, input().split())
h = list(map(int, input().split()))

DP = [float("inf")] * N
DP[0] = 0

for i in range(N):
    for j in range(1, K + 1):
        if N > i + j:
            DP[i + j] = min((DP[i] + abs(h[i] - h[i + j])), DP[i + j])

print(DP[-1])
