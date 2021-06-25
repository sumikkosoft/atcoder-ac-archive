import math

N, D = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for i in L:
    if D >= math.sqrt(i[0] ** 2 + i[1] ** 2):
        ans += 1

print(ans)
