N, M = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(M)]

for i in range(1000):
    s = str(i)
    flag = True
    if len(s) >= N:
        for j in X:
            if not s[j[0] - 1] == str(j[1]):
                flag = False
    else:
        flag = False

    if flag:
        print(s)
        exit()

print(-1)
