m, n, p = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = [list(map(int, input().split())) for _ in range(p)]

ans = min(a) + min(b)

for z in c:
    tmp = a[z[0] - 1] + b[z[1] - 1] - z[2]
    if tmp < ans:
        ans = tmp

print(ans)
