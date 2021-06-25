N = int(input())
p = list(map(int, input().split()))

ans = 0

for i in range(1, N - 1):
    if sorted([p[i - 1], p[i], p[i + 1]])[1] == p[i]:
        ans += 1

print(ans)
