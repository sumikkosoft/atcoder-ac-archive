import math

A, B, K = map(int, input().split())
tmp = []

for i in range(1, int(math.sqrt(max(A, B))) + 1):
    if A % i == 0:
        if B % i == 0:
            tmp.append(i)
        if B % (A // i) == 0:
            tmp.append(A // i)
tmp = list(set(tmp))
tmp.sort(reverse=True)

print(tmp[K - 1])
