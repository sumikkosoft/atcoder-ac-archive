a, b, c = map(int, input().split())
ans = 0
while True:
    if a == b == c:
        print(ans)
        exit()
    a, b, c = sorted([a, b, c])
    if a + 2 <= c:
        a += 2
    else:
        a += 1
        b += 1
    ans += 1
