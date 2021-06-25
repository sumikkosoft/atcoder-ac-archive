N, T = map(int, input().split())

ans = float("inf")
flag = False

for i in range(N):
    c, x = map(int, input().split())
    if T >= x:
        ans = min(ans, c)
        flag = True

if flag:
    print(ans)
else:
    print("TLE")
