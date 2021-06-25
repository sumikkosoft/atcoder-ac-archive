import math

N = int(input())
x = list(map(int, input().split()))

m = 0
u = 0
t = 0

for i in range(N):
    m += abs(x[i])
    u += abs(x[i]) ** 2
    x[i] = abs(x[i])

print(m)
print(math.sqrt(u))
print(max(x))
