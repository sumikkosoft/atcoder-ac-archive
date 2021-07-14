A, B, C = map(int, input().split())
N = int(input())
m = max(A, B, C)
ans = sum([A, B, C]) - m

for i in range(N):
    m *= 2

print(ans + m)
