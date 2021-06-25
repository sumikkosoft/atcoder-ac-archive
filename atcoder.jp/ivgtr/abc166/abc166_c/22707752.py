N, M = map(int, input().split())
H = list(map(int, input().split()))
tmp = [True] * N
R = [list(map(int, input().split())) for _ in range(M)]

for i in R:
    if H[i[0] - 1] > H[i[1] - 1]:
        tmp[i[1] - 1] = False
    elif H[i[0] - 1] < H[i[1] - 1]:
        tmp[i[0] - 1] = False
    else:
        tmp[i[1] - 1] = False
        tmp[i[0] - 1] = False


print(tmp.count(True))
