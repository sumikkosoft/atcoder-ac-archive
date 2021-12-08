import math

N = int(input())
A = [int(input()) for _ in range(N)]

ans = 0

A.sort(reverse=True)

for i in range(N):
    if i % 2 == 0:
        ans += A[i] ** 2
    else:
        ans -= A[i] ** 2

print(math.pi * ans)
