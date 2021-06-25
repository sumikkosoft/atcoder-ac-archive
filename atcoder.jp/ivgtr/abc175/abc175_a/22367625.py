s = input()

ans = s.count("R")
if ans == 2 and s[1] == "S":
    ans -= 1

print(ans)
