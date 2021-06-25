N = int(input())
X = [int(input()) for _ in range(N)]

tmp = [0] * N
pre = 0
ans = 0
while True:
    if tmp[pre] == 0:
        tmp[pre] += 1
        ans += 1
        if X[pre] == 2:
            print(ans)
            exit()
        else:
            pre = X[pre] - 1
    else:
        break

print(-1)
