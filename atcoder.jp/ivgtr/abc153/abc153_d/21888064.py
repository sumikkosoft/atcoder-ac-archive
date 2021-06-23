a = int(input())


def noo(tmp, tmp2, n):
    if n == 1:
        return tmp2 + 1

    tmp *= 2
    tmp2 += tmp
    return noo(tmp, tmp2, n // 2)


ans = noo(1, 0, a)


print(ans)
