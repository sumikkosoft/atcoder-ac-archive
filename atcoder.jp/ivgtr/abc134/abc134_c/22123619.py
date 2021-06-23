n = int(input())
a = [int(input()) for _ in range(n)]
_a = sorted(a)

for i in a:
    if i == _a[-1]:
        print(_a[-2])
    else:
        print(_a[-1])
