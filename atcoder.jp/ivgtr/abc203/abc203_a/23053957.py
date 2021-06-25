A = list(map(int, input().split()))

if A[0] == A[1]:
    print(A[2])
elif A[0] == A[2]:
    print(A[1])
elif A[1] == A[2]:
    print(A[0])
else:
    print(0)
