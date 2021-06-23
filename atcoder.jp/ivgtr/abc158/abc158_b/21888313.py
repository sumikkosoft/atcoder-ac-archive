x, a, b = map(int, input().split())
ans = 0

if x == 0:
    print(0)
    exit()

ans = ((x // (a + b)) * a) + min((x % (a + b)), a)

print(ans)
