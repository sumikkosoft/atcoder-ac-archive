N = int(input())
A = list(map(int, input().split()))
X = [0] * 8
over = 0
OVER_RATE = 3200

for i in range(N):
    if A[i] >= OVER_RATE:
        over += 1
    else:
        X[A[i] // 400] = 1

ans = sum(X)
mans = ans + over

ans = max(ans, 1)

print(ans, mans)
