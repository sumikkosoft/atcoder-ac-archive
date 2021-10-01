K = int(input())
A, B = input().split()


def nTo10(X, n):
    out = 0
    for i in range(1, len(str(X)) + 1):
        out += int(X[-i]) * (n ** (i - 1))
    return out


a = nTo10(A, K)
b = nTo10(B, K)

print(a * b)
