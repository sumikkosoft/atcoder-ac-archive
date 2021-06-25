N = int(input())
A = list(map(int, input().split()))
tmp = 0
ans = 0
MOD = 10 ** 9 + 7

for i in range(len(A) - 1):
    tmp += A[i]
    ans += tmp * A[i + 1]
    ans %= MOD

print(ans)
