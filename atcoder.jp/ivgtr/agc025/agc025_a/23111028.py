N = int(input())

if N % 10:
    before = str(N)[:1]
    after = list(map(int, str(N)[1:]))
    ans = int(before) + sum(after)
    print(ans)
else:
    print(10)
