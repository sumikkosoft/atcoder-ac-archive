import itertools

N = int(input())
S = list(map(int, input().split()))
A = sum(S)
ans = float("inf")
for i in itertools.accumulate(S[:-1]):
    ans = min(ans, abs(A - 2 * i))

print(ans)
