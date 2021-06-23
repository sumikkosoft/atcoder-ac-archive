import math

a, b, c, d = map(int, input().split())
ans = 0

k = int((c * d) / math.gcd(c, d))

ans += b - (b // c) - (b // d) + (b // k)
ans -= (a - 1) - ((a - 1) // c) - ((a - 1) // d) + ((a - 1) // k)
print(ans)
