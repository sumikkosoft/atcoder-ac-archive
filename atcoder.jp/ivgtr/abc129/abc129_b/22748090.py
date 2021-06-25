N = int(input())
x = list(map(int, input().split()))
ans = float("inf")

for i in range(N):
    ans = min(ans, abs(sum(x[:i]) - sum(x[i:])))

print(ans)
