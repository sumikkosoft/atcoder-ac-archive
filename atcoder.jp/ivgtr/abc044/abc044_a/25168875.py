N = int(input())
K = int(input())
X = int(input())
Y = int(input())

if N - K > 0:
    N -= K
    print(K * X + N * Y)
else:
    print(N * X)