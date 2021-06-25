N, M = map(int, input().split())
mi = float("inf")
mx = 0

for i in range(M):
    a, b = map(int, input().split())
    mx = max(mx, a)
    mi = min(mi, b)

print(mi - mx + 1) if mi - mx >= 0 else print(0)
