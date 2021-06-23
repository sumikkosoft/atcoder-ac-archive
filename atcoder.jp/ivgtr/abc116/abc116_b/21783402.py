n = int(input())
arr = [n]

ans = 1

while True:
    if arr.count(n) > 1:
        break

    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1

    arr.append(n)
    ans += 1

print(ans)
