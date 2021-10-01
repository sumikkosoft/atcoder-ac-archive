N = int(input())


def f(n, s):
    if n == 0:
        return s
    elif n % 2 == 0:
        return f(n // 2, s + "B")
    else:
        return f(n - 1, s + "A")


ans = f(N, "")

print(ans[::-1])
