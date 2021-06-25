import itertools
import math

N = int(input())
X = [list(map(int, input().split())) for _ in range(N)]
A = list(itertools.combinations(X, 2))

ans = 0

for i in A:
    ans = max(ans, (i[0][0] - i[1][0]) ** 2 + (i[0][1] - i[1][1]) ** 2)


print(math.sqrt(ans))
