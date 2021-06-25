X = input()
Y = input()
ans = 0
for i in range(len(X)):
    if not X[i] == Y[i]:
        ans += 1

print(ans)
