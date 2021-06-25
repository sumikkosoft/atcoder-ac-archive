N = int(input())
S = list(map(int, input().split()))
X = 3 ** N
A = []

for i in range(N):
    if S[i] % 2:
        A.append(1)
    else:
        A.append(2)

tmp = 1
for i in A:
    tmp *= i
print(X - tmp)
