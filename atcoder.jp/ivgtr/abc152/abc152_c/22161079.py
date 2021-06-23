n = int(input())
p = list(map(int, input().split()))
ans = 0
tmp = n + 1

for i in range(n):
    tmp = min(p[i], tmp)
    if p[i] == tmp:
        ans += 1

print(ans)
