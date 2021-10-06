H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
sum_H = [sum(i) for i in A]
sum_W = [sum(i) for i in zip(*A)]

for i in range(H):
    ans = []
    for j in range(W):
        ans.append(sum_H[i] + sum_W[j] - A[i][j])
    print(*ans)
