n, x = map(int, input().split())
A = list(map(int, input().split()))
_A = list()

for i in A:
    if not i == x:
        _A.append(i)

print(*_A)
