N, T = map(int, input().split())
A = [int(input()) for _ in range(N)]
prev = -10 * T
ans = 0

for i in A:
    if prev + T < i:
        ans += T
    else:
        ans += i - prev

    prev = i


print(ans)
