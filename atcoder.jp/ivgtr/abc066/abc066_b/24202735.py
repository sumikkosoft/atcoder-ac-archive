S = input()
L = len(S)

ans = 0

for i in range(2, L):
    if S[0 : i // 2] == S[i // 2 : i]:
        ans = i

print(ans)
