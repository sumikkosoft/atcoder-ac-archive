a = list(input())
ans = float("inf")

for i in range(len(a) - 2):
    tmp = abs(753 - int(a[i] + a[i + 1] + a[i + 2]))
    if ans > tmp:
        ans = tmp


print(ans)
