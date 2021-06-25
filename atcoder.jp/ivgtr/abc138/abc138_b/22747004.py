N = int(input())
B = list(map(int, input().split()))

ans = 0

for i in range(N):
    ans += 1 / B[i]


print(1 / ans)
