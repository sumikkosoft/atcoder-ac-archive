n, m = map(int, input().split())
x = [0 for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    x[a - 1] += 1
    x[b - 1] += 1

for i in x:
    print(i)
