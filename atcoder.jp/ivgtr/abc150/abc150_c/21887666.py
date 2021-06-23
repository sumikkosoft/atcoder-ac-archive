import itertools

x = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = sorted(a)
_a = 0
_b = 0
ans = 1

for i in itertools.permutations(m, x):
    if list(i) == a:
        _a = ans
    if list(i) == b:
        _b = ans
    if _a != 0 and _b != 0:
        break
    else:
        ans += 1

print(abs(_a - _b))
