X, Y, Z = map(int, input().split())
A = X * Y * Z

if A % 2:
    print(min((X * Y), (X * Z), (Y * Z)))
else:
    print(0)
