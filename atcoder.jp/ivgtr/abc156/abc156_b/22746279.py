N, K = map(int, input().split())
ans = 0


while N // K > 0:
    ans += 1
    N /= K

print(ans + 1)
