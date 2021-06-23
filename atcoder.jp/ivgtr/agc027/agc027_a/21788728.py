a, b = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = 0

for i in arr:
    if b < i:
        break
    ans += 1
    b -= i

else:
    if b > 0:
        ans -= 1

print(ans)
