N, M, X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_max = max(A)
B_min = min(B)

for i in range(X + 1, Y + 1):
    if A_max < i <= B_min:
        print("No War")
        exit()

print("War")
