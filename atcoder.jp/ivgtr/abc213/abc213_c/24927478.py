H, W, N = map(int, input().split())
X, Y = [], []

for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

_X = {x: i + 1 for i, x in enumerate(sorted(list(set(X))))}
_Y = {y: i + 1 for i, y in enumerate(sorted(list(set(Y))))}


for i in range(N):
    print(_X[X[i]], _Y[Y[i]])
