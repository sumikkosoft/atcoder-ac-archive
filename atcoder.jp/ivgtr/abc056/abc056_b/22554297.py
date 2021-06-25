W, a, b = map(int, input().split())

if a <= b <= a + W:
    print(0)
elif a < b:
    print(abs(b - a - W))
else:
    print(abs(b + W - a))
