a = int(input())
b = int(input())
c = list(map(int, input().split()))
ans = 0

for i in c:
    if i > b // 2:
        ans += (b - i) * 2
    else:
        ans += i * 2

print(ans)
