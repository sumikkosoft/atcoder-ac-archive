X, Y = map(int, input().split())


def check(N, a):
    if Y >= N:
        a += 1
        return check(N * 2, a)
    else:
        return a


print(check(X, 0))
