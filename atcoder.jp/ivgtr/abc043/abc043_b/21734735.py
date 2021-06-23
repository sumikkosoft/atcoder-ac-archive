a = input()

ans = ""

for i in range(len(a)):
    if a[i] == "B" and len(ans) > 0:
        ans = ans[:-1]
        continue
    if not a[i] == "B":
        ans += a[i]

print(ans)
