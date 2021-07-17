N, A, X, Y = map(int, input().split())

if N <= A:
    print(N * X)
else:
    N -= A
    print(A * X + N * Y)
