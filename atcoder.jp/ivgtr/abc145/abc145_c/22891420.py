import itertools
import math

N = int(input())
all = math.factorial(N)
tmp = list(itertools.permutations(range(N)))

A = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for i in tmp:
    tmp = 0
    for j in range(N - 1):
        tmp += (
            math.sqrt(
                abs(
                    (A[i[j]][0] - A[i[j + 1]][0]) ** 2
                    + (A[i[j]][1] - A[i[j + 1]][1]) ** 2
                )
            )
            / all
        )
    ans += tmp

print(ans)
