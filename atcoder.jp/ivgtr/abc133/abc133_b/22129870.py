import math

n, d = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]
x.append(x[0])
ans = 0

for i in range(len(x) - 1):
    for j in range(i + 1, len(x) - 1):
        if not i == j:
            tmp = 0
            for h in range(d):
                tmp += (x[i][h] - x[j][h]) ** 2
            tmp = math.sqrt(tmp)
            if tmp == int(tmp):
                ans += 1

print(ans)