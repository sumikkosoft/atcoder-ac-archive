X = [list(input().split()) for _ in range(4)]


for i in reversed(X):
    print(*i[::-1])
