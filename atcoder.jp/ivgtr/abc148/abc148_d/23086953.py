N = int(input())
A = list(map(int, input().split()))
ans = 0
if not A.count(1) > 0:
    print(-1)
    exit()
for i in range(N):
    if A[i] - 1 == ans:
        ans = A[i]

print(N - ans)
