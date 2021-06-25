N = int(input())
A = list(input().split())
tmp = dict()
ans = 0

for i in range(-200, 201):
    tmp.setdefault(str(i), 0)
    tmp[i] = A.count(str(i))

for i in range(-200, 201):
    for j in range(i + 1, 201):
        ans += tmp[i] * tmp[j] * ((i - j) ** 2)

print(ans)
