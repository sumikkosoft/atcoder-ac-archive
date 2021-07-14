A, B = map(int, input().split())


for i in range(1, 1001):
    now = (i + 1) * i // 2
    after = (i + 2) * (i + 1) // 2
    if B - A == after - now:
        print(now - A)
        break
