N = int(input())
A = list(map(int, input().split()))
s = 10 ** 9 + 7

A.sort()
ans = 1

for i in range(N):
    x = A[i] - i

    if x == 0:
        print(0)
        exit()
    ans = (ans * x) % s

print(ans)
