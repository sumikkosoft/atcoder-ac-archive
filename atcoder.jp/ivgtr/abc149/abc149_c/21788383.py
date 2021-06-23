n = int(input())
ans = 0

if n == 1 or n == 2:
    print(n)
    exit()


def check(m):
    tmp = 0
    for i in range(2, m):
        if m % i == 0:
            tmp = 0
            break
        else:
            tmp = i

    return tmp


for i in range(n, n + 100000):
    if i % 2:
        n = check(i)
        if n > 0:
            ans = i
            break

print(ans)
