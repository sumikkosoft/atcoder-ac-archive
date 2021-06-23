n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
a.append(n + a[0])

ans = 0

for i in range(len(a) - 1):
    if a[i + 1] - a[i] >= ans:
        ans = a[i + 1] - a[i]


print(n - ans)
