x = int(input())
y = list(input())
ans = 0
tmp = 0

for i in y:
    if i == "I":
        tmp += 1
    else:
        tmp -= 1

    if ans < tmp:
        ans = tmp

print(ans)
