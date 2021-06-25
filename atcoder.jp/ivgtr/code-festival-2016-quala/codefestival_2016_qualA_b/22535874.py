N = int(input())
A = list(map(int, input().split()))
ans = 0

for i in range(len(A)):
    if A[A[i] - 1] == i + 1:
        ans += 1
        A[i] = 0

print(ans)
