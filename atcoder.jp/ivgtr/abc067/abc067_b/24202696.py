N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse=True)
ans = 0
for i in range(K):
    ans += A[i]

print(ans)
