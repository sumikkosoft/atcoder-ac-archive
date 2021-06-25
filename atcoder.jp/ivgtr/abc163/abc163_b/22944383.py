M, N = map(int, input().split())
S = list(map(int, input().split()))

if sum(S) > M:
    print(-1)
else:
    print(M - sum(S))
