import math

A, B, H, M = map(int, input().split())
radian = math.radians(abs(30 * (H + M / 60) - 6 * M))

ans = (A ** 2 + B ** 2 - 2 * A * B * math.cos(radian)) ** 0.5

print(ans)
