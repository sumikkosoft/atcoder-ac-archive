N = int(input())
X = list()

for i in range(N):
    tmp = list()
    for j in range(N):
        tmp.append("")
    X.append(tmp)

for i in reversed(range(N)):
    S = list(input())
    for index, j in enumerate(S):
        X[index][i] = j

for i in X:
    print("".join(i))
