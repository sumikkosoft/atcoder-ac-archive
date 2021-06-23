a, b, c, x, y = map(int, input().split())


ans = min(
    a * x + b * y,
    a * (x - min(x, y)) + b * (y - min(x, y)) + c * min(x, y) * 2,
    c * max(x, y) * 2,
)

print(ans)
