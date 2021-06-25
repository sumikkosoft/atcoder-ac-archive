N, K = map(int, input().split())

for i in range(K):
    tmp = list(str(N))
    g1 = int("".join(sorted(tmp, reverse=True)))
    g2 = int("".join(sorted(tmp)))
    N = g1 - g2

print(N)
