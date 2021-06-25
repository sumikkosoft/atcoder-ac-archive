S = input()

tmp = now = ""
ans = 0

for i in S:
    now += i
    if tmp != now:
        tmp = now
        now = ""
        ans += 1

print(ans)
