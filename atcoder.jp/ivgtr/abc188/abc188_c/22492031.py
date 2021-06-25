N = int(input())
A = list(map(int, input().split()))

before = max(A[: 2 ** (N - 1)])
after = max(A[2 ** (N - 1) :])


if before > after:
    print(A.index(after) + 1)
else:
    print(A.index(before) + 1)
