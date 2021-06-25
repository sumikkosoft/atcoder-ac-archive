N = int(input())
A, B, C = (
    list(map(int, input().split())),
    list(map(int, input().split())),
    list(map(int, input().split())),
)
ans = 0
_A = [0] * N

for i in range(N):
    _A[A[i] - 1] += 1


for i in range(N):
    ans += _A[B[C[i] - 1] - 1]

print(ans)
