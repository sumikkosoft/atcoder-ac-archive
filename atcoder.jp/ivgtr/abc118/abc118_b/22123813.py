n, m = map(int, input().split())
ans = 0
x = list()
for i in range(n):
    arr = list(map(int, input().split()))
    for i2 in range(1, len(arr)):
        x.append(arr[i2])

for i in range(1, m + 1):
    if x.count(i) == n:
        ans += 1

print(ans)
