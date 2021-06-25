N = int(input())
ans = 0

for i in range(1, N):
    tmp = (N - 1) // i
    ans += tmp

print(ans)
