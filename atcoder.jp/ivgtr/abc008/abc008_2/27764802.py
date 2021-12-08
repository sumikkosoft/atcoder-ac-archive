N = int(input())
X = {}

for i in range(N):
    x = input()
    X.setdefault(x, 0)
    X[x] += 1

ans = sorted(X.items(), key=lambda x: x[1], reverse=True)

print(ans[0][0])
