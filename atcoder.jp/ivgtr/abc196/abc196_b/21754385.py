a = input()
ans = ""
if a.find("."):
    ans = a.split(".")[0]
else:
    ans = a
print(ans)
