N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

dp = [float("inf")] * N
dp[0] = T[0]

for i in range(2 * N):
    dp[(i + 1) % N] = min(T[(i + 1) % N], dp[(i % N)] + S[(i % N)])

for i in dp:
    print(i)
