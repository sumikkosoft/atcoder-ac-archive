N, X = map(int, input().split())
A = list(map(int, input().split()))


def Base_10_to_n(X, n):
    if int(X / n):
        return Base_10_to_n(int(X / n), n) + str(X % n)
    return str(X % n)


x = list(Base_10_to_n(X, 2))
x.reverse()

ans = 0

for i in range(len(x)):
    if x[i] == "1":
        ans += A[i]

print(ans)
