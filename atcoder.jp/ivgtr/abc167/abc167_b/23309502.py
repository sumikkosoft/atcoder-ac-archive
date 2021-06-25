A, B, C, K = map(int, input().split())
a = 1
c = -1

ans = 0

if K > A:
    K -= A
    ans += A * a
    if K > B:
        K -= B
        ans += K * c
else:
    ans += K * a

print(ans)
