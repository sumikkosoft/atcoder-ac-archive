W = list(input())
ans = ""
for i in W:
    if not (i == "a" or i == "e" or i == "i" or i == "o" or i == "u"):
        ans += i

print(ans)
