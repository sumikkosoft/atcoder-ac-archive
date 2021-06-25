N = int(input())
NG = [int(input()) for _ in range(3)]


def check(n, tmp):
    if n not in NG:
        if tmp <= 100:
            if n <= 0:
                return True
            else:
                tmp += 1
                if n - 3 not in NG:
                    return check(n - 3, tmp)
                elif n - 2 not in NG:
                    return check(n - 2, tmp)
                elif n - 1 not in NG:
                    return check(n - 1, tmp)
                else:
                    return False
        else:
            return False
    else:
        return False


if check(N, 0):
    print("YES")
else:
    print("NO")
