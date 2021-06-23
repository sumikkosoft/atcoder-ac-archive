import copy

n = int(input())
t = list(map(int, input().split()))
m = int(input())
for i in range(m):
    p, x = map(int, input().split())
    _t = copy.copy(t)
    _t[p - 1] = x
    print(sum(_t))
