N, K = map(int, input().split())
P = [int(input()) for _ in range(N)]
ans = 0

if 0 in P:
    ans = N
else:
    right, left = 0, 0
    tmp = 1
    while right < N:
        if tmp * P[right] <= K:
            tmp *= P[right]
            right += 1
            ans = max(ans, right - left)
        elif right == left:
            right += 1
            left += 1
        else:
            tmp //= P[left]
            left += 1


print(ans)
