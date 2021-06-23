n = int(input())
x = [input() for _ in range(n)]
ans = "Yes"
for i in range(len(x)):
    if x.count(x[i]) > 1:
        ans = "No"
    if not i + 1 == len(x):
        if not x[i + 1][0] == x[i][-1]:
            ans = "No"

print(ans)
