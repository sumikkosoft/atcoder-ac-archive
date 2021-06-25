import math

N = int(input())
ans = math.factorial(N) % (10 ** 9 + 7)


print(ans)
