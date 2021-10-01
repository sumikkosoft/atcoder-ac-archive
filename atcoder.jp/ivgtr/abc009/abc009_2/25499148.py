N = int(input())
X = list(set(int(input()) for _ in range(N)))

X.sort()

print(X[-2])
