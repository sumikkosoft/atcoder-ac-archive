N = int(input())
ans = 0


for i in range(N):
    N, K = map(int, input().split())
    ans += K - N + 1

print(ans)
