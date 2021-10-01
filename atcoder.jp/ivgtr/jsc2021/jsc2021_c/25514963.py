A, B = map(int, input().split())
ans = 0

for p in reversed(range(1, B + 1)):
    nA = (A // p + (A % p != 0)) * p
    if nA <= B and nA + p <= B:
        ans = p
        break

print(ans)
