N, D = map(int, input().split())
L = list(map(int, input().split()))
L.sort()
ans = 0

for i in range(D):
    ans += L[i]

print(ans)
