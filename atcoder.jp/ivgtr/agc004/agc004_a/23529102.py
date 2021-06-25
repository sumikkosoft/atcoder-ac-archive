X, Y, Z = map(int, input().split())
A = X * Y * Z

if A % 2:
    x = X // 2
    y = Y // 2
    z = Z // 2
    print(min((A - x * Y * Z * 2), (A - X * y * Z * 2), (A - X * Y * z * 2)))
else:
    print(0)
