N, X = map(int, input().split())
m = [int(input()) for _ in range(N)]
m.sort()

X -= sum(m)
ans = len(m)
ans += X // m[0]
print(ans)
