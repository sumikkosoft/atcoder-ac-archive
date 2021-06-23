h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h)]

tmp = 100
ans = 0

for i in A:
    tmp = min(tmp, min(i))

for i in range(h):
    for j in range(w):
        ans += A[i][j] - tmp

print(ans)
