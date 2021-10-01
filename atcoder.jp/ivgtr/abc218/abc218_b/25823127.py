A = list(map(int, input().split()))

X = "abcdefghijklmnopqrstuvwxyz"
ans = ""

for i in A:
    ans += X[i - 1]

print(ans)
