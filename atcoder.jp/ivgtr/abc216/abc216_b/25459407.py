N = int(input())
X = [list(input().split()) for _ in range(N)]

D = dict()

for i in X:
    x = i[0] + "+" + i[1]
    D.setdefault(x, 0)
    D[x] += 1

sortD = sorted(D.values(), reverse=True)

if sortD[0] > 1:
    print("Yes")
else:
    print("No")
