n, m = map(int, input().split())
x = list()
for _ in range(m):
    a, b = map(int, input().split())
    x.append([a, b])
sita = 0
ue = n

for i in x:
    sita = max(sita, i[0])
    ue = min(ue, i[1])

if ue - sita + 1 <= 0:
    print(0)
    exit()

print(ue - sita + 1)
