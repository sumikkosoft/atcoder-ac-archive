n = int(input())
L = list()
ans = 0
for _ in range(n):
    x, y = map(int, input().split())
    L.append([x, y])

for i in range(n):
    for j in range(i + 1):
        if i == j:
            continue

        if -1 <= (L[j][1] - L[i][1]) / (L[j][0] - L[i][0]) <= 1:
            ans += 1


print(ans)
