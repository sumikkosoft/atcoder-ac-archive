n = int(input())
ans = list()

for i in range(n):
    a, p, x = map(int, input().split())
    if x - a > 0:
        ans.append(p)

if len(ans):
    print(min(ans))
else:
    print(-1)
