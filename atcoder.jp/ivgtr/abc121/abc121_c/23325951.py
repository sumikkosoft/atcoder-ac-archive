N, M = map(int, input().split())
Ar = [list(map(int, input().split())) for _ in range(N)]
Ar.sort()

ans = 0

for item in Ar:
    if M > item[1]:
        M -= item[1]
        ans += item[0] * item[1]
    else:
        ans += item[0] * M
        print(ans)
        exit()
