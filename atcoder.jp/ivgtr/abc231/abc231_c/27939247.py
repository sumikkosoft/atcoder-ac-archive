import bisect

N, Q = map(int, input().split())
A = list(map(int, input().split()))
X = [int(input()) for _ in range(Q)]

A.sort()

for i in range(Q):
    x = X[i]
    S = bisect.bisect_left(A, x)

    print(N - S)
