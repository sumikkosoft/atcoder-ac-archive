S = list(input())
ans = list()

for i in range(len(S)):
    if i % 2 == 0:
        ans.append(S[i])

print("".join(ans))
