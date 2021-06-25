N, K = map(int, input().split())
tmp = [False] * N
for i in range(K):
    d = int(input())
    a = list(map(int, input().split()))
    for j in range(d):
        tmp[a[j] - 1] = True

print(tmp.count(False))
