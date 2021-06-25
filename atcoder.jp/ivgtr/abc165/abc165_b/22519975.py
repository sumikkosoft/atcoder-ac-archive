tmp = 100
X = int(input())
ans = 0

while tmp < X:
    tmp += tmp // 100
    ans += 1

print(ans)
