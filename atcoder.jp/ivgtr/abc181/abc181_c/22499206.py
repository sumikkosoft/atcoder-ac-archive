N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            x1, y1 = S[i]
            x2, y2 = S[j]
            x3, y3 = S[k]
            if (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1):
                print("Yes")
                exit()

print("No")
