S = input()
T = input()
ans = float("inf")

for i in range(len(S) - len(T) + 1):
    tmp = 0
    for j in range(len(T)):
        if not S[i + j] == T[j]:
            tmp += 1
    ans = min(ans, tmp)

print(ans)
