N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)

for i in range(N):
    if A[i] < K:
        print(i)
        exit()

print(N)
