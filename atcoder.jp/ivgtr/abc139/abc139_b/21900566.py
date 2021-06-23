a, b = map(int, input().split())
ans = 0

for i in range(0, 100):
    if b == 1:
        break
    if (a - 1) * i + a >= b:
        ans = i + 1
        break

print(ans)
