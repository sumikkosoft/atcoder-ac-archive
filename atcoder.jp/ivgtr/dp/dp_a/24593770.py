N = int(input())
A = list(map(int, input().split()))

DP = [0] * (N)
DP[0] = 0
DP[1] = abs(A[0] - A[1])

for i in range(2, N):
    DP[i] = min(DP[i - 1] + abs(A[i - 1] - A[i]), DP[i - 2] + abs(A[i - 2] - A[i]))

print(DP[-1])
