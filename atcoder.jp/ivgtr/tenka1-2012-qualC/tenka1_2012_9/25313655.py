N = int(input())
ans = 0


def sosu(x):
    if x == 1:
        return False
    for j in range(2, int(x ** 0.5) + 1):
        if x % j == 0:
            return False

    return True


for i in range(1, N):
    if sosu(i):
        ans += 1


print(ans)
