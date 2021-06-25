N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
tmp = sum(A) / (4 * M)

for i in range(M):
    if A[i] < tmp:
        print("No")
        exit()

print("Yes")
