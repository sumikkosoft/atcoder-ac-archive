N = int(input())
S = list(map(int, input().split()))
ans = 0
for i in range(0, N, 2):
    if S[i] % 2:
        ans += 1

print(ans)
