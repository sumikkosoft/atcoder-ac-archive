a, b, c = map(int, input().split())
arr = list(map(int, input().split()))
arrr = list()
for _ in range(a):
    arrr.append(list(map(int, input().split())))

ans = 0

for b in arrr:
    v = 0
    for i in range(len(arr)):
        v += b[i] * arr[i]
    if v + c > 0:
        ans += 1

print(ans)
