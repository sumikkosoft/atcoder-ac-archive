X, K, D = map(int, input().split())
X = abs(X)
r = X % D

if X - r > K * D:
    print(X - K * D)
else:
    n = X // D
    if (K - n) % 2:
        print(abs(r - D))
    else:
        print(r)
