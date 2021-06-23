a = int(input())
arr = list(map(int, input().split()))
ans = float("inf")

for i in range(1, 100):
    tmp = 0
    for x in arr:
        tmp += (x - i) ** 2
    if ans > tmp:
        ans = tmp

print(ans)
