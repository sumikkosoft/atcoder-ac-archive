N = int(input())
b = [input() for _ in range(N)]
M = int(input())
r = [input() for _ in range(M)]

B = {}
R = {}

for i in b:
    B.setdefault(i, 0)
    R.setdefault(i, 0)
    B[i] += 1

for i in r:
    R.setdefault(i, 0)
    R[i] -= 1

ans = 0

for i in B:
    ans = max(ans, (B[i] + R[i]))


print(ans)
