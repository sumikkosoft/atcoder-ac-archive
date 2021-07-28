S = input()
LEN_S = len(S)
MOD = 10 ** 9 + 7
chokudai = "chokudai"
LEN_C = len(chokudai)

dp = [[0 for _ in range(LEN_C + 1)] for _ in range(LEN_S + 1)]

for i in range(LEN_S + 1):
    dp[i][0] = 1

for i in range(LEN_S):
    for j in range(LEN_C):
        if S[i] == chokudai[j]:
            dp[i + 1][j + 1] = (dp[i][j] + dp[i][j + 1]) % MOD
        else:
            dp[i + 1][j + 1] = dp[i][j + 1]


print(dp[-1][-1])
