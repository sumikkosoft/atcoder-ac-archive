X, N = map(int, input().split())
p = list(map(int, input().split()))
ans = 0

for i in range(51):
    tmp = X - i
    if tmp not in p:
        ans = tmp
        break
    tmp = X + i
    if tmp not in p:
        ans = tmp
        break

print(ans)
