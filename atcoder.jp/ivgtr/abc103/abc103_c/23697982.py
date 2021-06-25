N = int(input())
S = list(map(int, input().split()))

ans = 0

for i in S:
    ans += i - 1

print(ans)
