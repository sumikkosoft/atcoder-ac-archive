from collections import Counter

N = int(input())
A = list(map(int, input().split()))
C = Counter(A)
answer = (N * (N - 1)) // 2
for i in C.keys():
    if C[i] > 1:
        answer -= (C[i] * (C[i] - 1)) // 2

print(answer)
