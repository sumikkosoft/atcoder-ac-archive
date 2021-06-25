A = list(map(int, input().split()))

if A[0] == A[1]:
    print(A[0])
elif 0 not in A:
    print(0)
elif 1 not in A:
    print(1)
else:
    print(2)
