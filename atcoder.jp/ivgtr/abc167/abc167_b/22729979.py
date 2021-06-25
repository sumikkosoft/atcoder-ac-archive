A, B, C, K = map(int, input().split())

ans = 0

if A < K:
    ans += A
    K -= A
else:
    ans += K
    print(ans)
    exit()


if B < K:
    K -= B
else:
    print(ans)
    exit()


if C < K:
    ans -= A
else:
    ans -= K
    print(ans)
    exit()


print(ans)
