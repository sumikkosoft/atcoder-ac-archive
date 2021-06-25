X = input()
before = X[: len(X) // 2]
after = X[len(X) // 2 + 1 :]

if before == after:
    print("Yes")
else:
    print("No")
