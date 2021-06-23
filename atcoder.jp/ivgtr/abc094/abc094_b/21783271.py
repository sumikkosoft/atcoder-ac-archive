n, m, x = map(int, input().split())
arr = list(map(int, input().split()))

high = 0
low = 0

for i in arr:
    if i > x:
        high += 1
    else:
        low += 1

print(min(high, low))
