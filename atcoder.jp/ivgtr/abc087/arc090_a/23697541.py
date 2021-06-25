N = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))

leftTop = A1[0]
rightBottom = A2[-1]

sumA1 = 0
sumA2 = sum(A2)
ans = []

for i in range(N):
    sumA1 += A1[i]
    ans.append(sumA1 + sumA2)
    sumA2 -= A2[i]

print(max(ans))
