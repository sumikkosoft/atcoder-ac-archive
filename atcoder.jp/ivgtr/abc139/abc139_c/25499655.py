N = int(input())
A = list(map(int, input().split()))
ans = 0
tmp = 0
prev = A[0]

for i in range(1, N):
    if prev >= A[i]:
        tmp += 1
    else:
        tmp = 0
    prev = A[i]
    ans = max(ans, tmp)


print(ans)
