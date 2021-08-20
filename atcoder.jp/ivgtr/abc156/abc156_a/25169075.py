N, R = map(int, input().split())

if 10 > N:
    X = 100 * (10 - N)
    print(X + R)
else:
    print(R)
