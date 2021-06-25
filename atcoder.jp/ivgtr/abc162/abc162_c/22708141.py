import math

N = int(input())
ans = 0

for i in range(1, N + 1):
    for j in range(1, N + 1):
        tmp = math.gcd(i, j)
        for k in range(1, N + 1):
            ans += math.gcd(tmp, k)

print(ans)
