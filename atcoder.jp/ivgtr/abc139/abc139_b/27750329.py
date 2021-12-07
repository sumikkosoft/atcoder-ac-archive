import math

A, B = map(int, input().split())

if B <= 1:
    print(0)
    exit()

if A >= B:
    print(1)
    exit()

B -= A

ans = math.ceil(B / (A - 1)) + 1

print(ans)
