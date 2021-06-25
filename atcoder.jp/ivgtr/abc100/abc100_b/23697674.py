D, N = map(int, input().split())

x = 1

if D == 1:
    x = 100
elif D == 2:
    x = 10000

if N == 100:
    N += 1

ans = x * N


print(ans)
