a = int(input())
b, c = map(int, input().split())
arr = [int(input()) for i in range(a)]
ans = c


for i in arr:
    for x in range(0, 100):
        y = x * i + 1

        if y > b:
            break
        else:
            ans += 1


print(ans)
