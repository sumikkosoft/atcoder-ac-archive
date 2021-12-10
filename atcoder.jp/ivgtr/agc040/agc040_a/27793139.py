S = input()
L = len(S)
A = [0] * (L + 1)
tmp = 1
for i in range(L):
    if S[i] == "<":
        A[i + 1] = tmp
        tmp += 1
    else:
        tmp = 1

tmp = 1

for i in range(L - 1, -1, -1):
    if S[i] == ">":
        A[i] = max(A[i], tmp)
        tmp += 1
    else:
        tmp = 1

print(sum(A))
