N = int(input())

a, b, c = 0, 0, 1

if N == 1:
    print(0)
elif N == 2:
    print(0)
else:
    x = 0
    for i in range(3, N):
        x = (a + b + c) % 10007
        a = b
        b = c
        c = x

    print(c)
