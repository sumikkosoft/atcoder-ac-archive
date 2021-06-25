X, N = map(int, input().split())
P = list(map(int, input().split()))

for i in range(0, 101):
    if X - i not in P:
        print(X - i)
        exit()
    if X + i not in P:
        print(X + i)
        exit()
