import itertools

N, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

tmp = list(itertools.permutations(range(N - 1)))
ans = 0


for i in tmp:
    L = A[0][i[0] + 1] + A[i[-1] + 1][0]
    for j in range(1, N - 1):
        L += A[i[j - 1] + 1][i[j] + 1]

    if L == K:
        ans += 1

print(ans)
