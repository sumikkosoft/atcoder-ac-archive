a, b = map(int, input().split())

n = 0

while True:
    if b == 1:
        break
    n += 1

    if (n - 1) * (a - 1) + a >= b:
        break

print(n)
