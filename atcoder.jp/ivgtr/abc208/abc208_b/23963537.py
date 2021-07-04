import math

N = int(input())
i = 1
ans = 0

while N > 0:
    if N < math.factorial(i):
        x = math.factorial(i - 1)
        tmp = N // x
        N -= x * tmp
        i -= 1
        ans += tmp
    else:
        i += 1

print(ans)
