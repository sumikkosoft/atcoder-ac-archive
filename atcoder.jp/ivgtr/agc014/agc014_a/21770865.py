a, b, c = map(int, input().split())
ans = 0
for _ in range(0, max([a, b, c])):
    if a == b == c and not a % 2:
        ans = -1
        break
    if not a % 2 and not b % 2 and not c % 2:
        ans += 1
        _a = (b + c) // 2
        _b = (a + c) // 2
        _c = (a + b) // 2
        a = _a
        b = _b
        c = _c
    else:
        break


print(ans)
