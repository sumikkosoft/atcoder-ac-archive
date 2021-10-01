a, b = map(int, input().split())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

X = [
    {
        7: "x",
        8: "x",
        9: "x",
        0: "x",
    },
    {
        4: "x",
        5: "x",
        6: "x",
    },
    {
        2: "x",
        3: "x",
    },
    {
        1: "x",
    },
]

for i in range(a):
    for j in range(len(X)):
        if A[i] in X[j]:
            X[j][A[i]] = "."

for i in range(b):
    for j in range(len(X)):
        if B[i] in X[j]:
            X[j][B[i]] = "o"

for i in range(len(X)):
    print(" " * i + " ".join(X[i].values()))
