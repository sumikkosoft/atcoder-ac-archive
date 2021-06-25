N = int(input())
S = list(map(int, input().split()))

DP = [0] * N
DP[0] = 0
DP[1] = abs(S[1] - S[0])

for i in range(2, N):
    DP[i] = min((abs(S[i] - S[i - 1]) + DP[i - 1]), (abs(S[i] - S[i - 2]) + DP[i - 2]))

print(DP[-1])
