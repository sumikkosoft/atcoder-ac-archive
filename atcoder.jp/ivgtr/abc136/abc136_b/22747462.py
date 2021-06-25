S = int(input())
ans = 0

for i in range(1, S + 1):
    if 1 <= i < 10:
        ans += 1
    elif 100 <= i < 1000:
        ans += 1
    elif 10000 <= i < 100000:
        ans += 1

print(ans)
