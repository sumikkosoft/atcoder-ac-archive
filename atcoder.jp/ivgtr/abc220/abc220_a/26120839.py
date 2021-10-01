A, B, C = map(int, input().split())
ans = -1

for i in range(1, 1001):
    if A <= C * i <= B:
        ans = C * i

print(ans)
