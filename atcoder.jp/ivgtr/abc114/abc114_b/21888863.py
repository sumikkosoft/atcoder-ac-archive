a = input()
ans = float("inf")

for i in range(len(a) - 2):
    tmp = abs(753 - int(a[i : i + 3]))
    if ans > tmp:
        ans = tmp


print(ans)
