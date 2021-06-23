n = int(input())
x = list(map(int, input().split()))

maxx = max(x)
minx = min(x)

n = float("inf")

for p in range(minx, maxx + 1):
    tmp = 0
    for i in range(len(x)):
        tmp += (x[i] - p) ** 2
    if n > tmp:
        n = tmp
print(n)
