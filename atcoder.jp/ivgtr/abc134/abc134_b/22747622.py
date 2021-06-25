import math

N, D = map(int, input().split())
D = 2 * D + 1

print(math.ceil(N / D))
