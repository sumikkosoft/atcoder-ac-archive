n, m, t = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(m)]
ans = "Yes"
tmp = n
for i in range(m):
    if i == 0:
        n -= A[i][0]
    else:
        n -= A[i][0] - A[i - 1][1]

    if n <= 0:
        ans = "No"

    if tmp >= n + A[i][1] - A[i][0]:
        n += A[i][1] - A[i][0]
    else:
        n = tmp

n -= t - A[-1][1]
if n <= 0:
    ans = "No"

print(ans)
