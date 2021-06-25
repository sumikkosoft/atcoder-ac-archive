Q, H, S, D = map(int, input().split())
N = int(input())

n = N // 2

ans = min(Q * 8 * n, H * 4 * n, S * 2 * n, D * n)

if N % 2:
    ans += min(Q * 4, H * 2, S)

print(ans)
