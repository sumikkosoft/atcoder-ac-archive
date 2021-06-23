h, w, x, y = map(int, input().split())
s = [input() for _ in range(h)]
x, y = x - 1, y - 1
ans = 1
flagE = True
flagN = True
flagW = True
flagS = True

for i in range(1, 100):
    if flagE and x - i >= 0:
        if s[x - i][y] == ".":
            ans += 1
        else:
            flagE = False
    if flagN and y + i < w:
        if s[x][y + i] == ".":
            ans += 1
        else:
            flagN = False
    if flagW and x + i < h:
        if s[x + i][y] == ".":
            ans += 1
        else:
            flagW = False
    if flagS and y - i >= 0:
        if s[x][y - i] == ".":
            ans += 1
        else:
            flagS = False

print(ans)
