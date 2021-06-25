import math
from functools import reduce


def my_lcm_base(x, y):
    return (x * y) // math.gcd(x, y)


def my_lcm(*numbers):
    return reduce(my_lcm_base, numbers, 1)


N = int(input())
S = list(map(int, input().split()))

ans = 0
lcm = my_lcm(*S) - 1

for i in S:
    ans += lcm % i

print(ans)
