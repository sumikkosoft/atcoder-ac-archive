H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]
ans = 0
for i in range(H):
    for j in range(W):
        if A[i][j] == ".":
            if j < W - 1:
                if A[i][j + 1] == ".":
                    ans += 1
            if i < H - 1:
                if A[i + 1][j] == ".":
                    ans += 1

print(ans)
