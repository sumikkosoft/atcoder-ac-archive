N = int(input())
A = list(map(int, input().split()))
X = int(input())

Y = X // sum(A)
Z = Y * sum(A)
ans = Y * N

for i in A:
    Z += i
    if Z > X:
        print(ans + 1)
        exit()
    else:
        ans += 1
