N = int(input())
A = list(map(int, input().split()))

ans = (N * (N - 1)) // 2
A.sort()
tmp = 0
stack = 0

for i in A:
    if tmp == i:
        stack += 1
    else:
        if stack > 1:
            ans -= (stack * (stack - 1)) // 2
        tmp = i
        stack = 1

if stack > 1:
    ans -= (stack * (stack - 1)) // 2

print(ans)
