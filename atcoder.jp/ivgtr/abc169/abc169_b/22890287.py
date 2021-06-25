N = int(input())
A = list(map(int, input().split()))
ans = 1

A.sort(reverse=True)
if A[-1] == 0:
    print(0)
    exit()   

for i in range(N):
    if len(str(ans * A[i] - 1)) > 18:
        print(-1)
        exit()
    ans *= A[i]


print(ans)
