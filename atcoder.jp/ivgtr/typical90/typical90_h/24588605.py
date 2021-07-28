N = int(input())
S = input()
MOD = 10 ** 9 + 7
atcoder = "atcoder"
LEN_A = len(atcoder)

dp = [[0 for _ in range(LEN_A + 1)] for _ in range(N + 1)]

for i in range(N + 1):
    dp[i][0] = 1

for i in range(N):
    for j in range(LEN_A):
        if S[i] == atcoder[j]:
            dp[i + 1][j + 1] = (dp[i][j] + dp[i][j + 1]) % MOD
        else:
            dp[i + 1][j + 1] = dp[i][j + 1]


print(dp[-1][-1])
