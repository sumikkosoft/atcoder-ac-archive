N = int(input())
A = list(map(int, input().split()))
ans = 0
ans2 = 0

for i in range(2, 1000):
    tmp = 0
    for j in range(N):
        if A[j] % i == 0:
            tmp += 1
    if ans2 < tmp:
        ans2 = tmp
        ans = i

print(ans)
