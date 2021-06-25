N, K = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

AB.sort()
ans = 0
flag = True

for i in range(N):
    now = AB[i][0] - ans
    if now <= K:
        K -= now
        K += AB[i][1]
        ans = AB[i][0]
    else:
        ans += K
        flag = False
        break

if flag:
    ans += K

print(ans)
