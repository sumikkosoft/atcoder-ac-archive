H, W = map(int, input().split())
X = [list(input()) for _ in range(H)]

for i in range(H):
    for j in range(W):
        if X[i][j] == ".":
            tmp = 0
            if i > 0 and j > 0 and X[i - 1][j - 1] == "#":
                tmp += 1
            if j > 0 and X[i][j - 1] == "#":
                tmp += 1
            if H - 1 > i and j > 0 and X[i + 1][j - 1] == "#":
                tmp += 1
            if i > 0 and X[i - 1][j] == "#":
                tmp += 1
            if H - 1 > i and X[i + 1][j] == "#":
                tmp += 1
            if i > 0 and W - 1 > j and X[i - 1][j + 1] == "#":
                tmp += 1
            if W - 1 > j and X[i][j + 1] == "#":
                tmp += 1
            if H - 1 > i and W - 1 > j and X[i + 1][j + 1] == "#":
                tmp += 1
            X[i][j] = str(tmp)


for i in X:
    print("".join(i))
