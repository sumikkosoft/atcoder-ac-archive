import copy

N = int(input())
m = list(map(int, input().split()))
x = copy.deepcopy(m)
x.sort(reverse=True)

print(m.index(x[1]) + 1)
