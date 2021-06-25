N = int(input())
ans = 0

A = N // 500

ans += 1000 * A
N -= 500 * A

B = N // 5

ans += 5 * B

print(ans)
