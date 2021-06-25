N, L = map(int, input().split())
tmp = []
ans = float("inf")

for i in range(N):
    if min(abs(ans), abs(i + L)) == abs(i + L):
        ans = i + L
    tmp.append(i + L)

print(sum(tmp) - ans)
