x, y = map(int, input().split())
if x == 1 or y == 1:
    print("1")
    exit()
ans = (x * y + 1) // 2
print(ans)
