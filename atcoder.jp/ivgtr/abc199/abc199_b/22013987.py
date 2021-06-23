a = int(input())
b = list(map(int, input().split()))
c = list(map(int, input().split()))
maxmin = max(min(b), min(c))
minmax = min(max(b), max(c))

if maxmin - minmax + 1 > 0:
    print(maxmin - minmax + 1)
else:
    print(0)
