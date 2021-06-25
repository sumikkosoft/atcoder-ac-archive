import math

N, X, Y = map(int, input().split())


r = math.sqrt(X ** 2 + Y ** 2)

if r < N:
    print(2)
else:
    print(math.ceil(r / N))
