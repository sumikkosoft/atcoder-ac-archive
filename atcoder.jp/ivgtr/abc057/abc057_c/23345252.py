import math

N = int(input())
ans = float("inf")

for i in range(1, int(math.sqrt(N)) + 1):
    if N % i == 0:
        ans = min(ans, max(len(str(i)), len(str(N // i))))

print(ans)
