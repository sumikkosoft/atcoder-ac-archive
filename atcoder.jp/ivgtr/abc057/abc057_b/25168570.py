N, M = map(int, input().split())

seito = [list(map(int, input().split())) for _ in range(N)]
point = [list(map(int, input().split())) for _ in range(M)]
ans = [float("inf")] * N

for i in range(N):
    tmp = float("inf")

    for j in range(M)[::-1]:
        x = abs(seito[i][0] - point[j][0]) + abs(seito[i][1] - point[j][1])
        if x <= tmp:
            tmp = x
            ans[i] = j


for i in ans:
    print(i + 1)
