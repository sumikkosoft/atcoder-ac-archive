import itertools
import math

N = int(input())
all = math.factorial(N)
tmp = list(itertools.permutations(range(N), 2))

A = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for i in tmp:
    ans += math.sqrt((A[i[0]][0] - A[i[1]][0]) ** 2 + (A[i[0]][1] - A[i[1]][1]) ** 2)

print(ans / N)
