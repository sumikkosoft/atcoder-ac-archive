N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
B = [list(map(int, input().split())) for _ in range(Q)]

S1 = [0] * (N + 1)
S2 = [0] * (N + 1)

for i in range(1, N + 1):
    if A[i - 1][0] == 1:
        S1[i] = S1[i - 1] + A[i - 1][1]
        S2[i] = S2[i - 1]
    else:
        S2[i] = S2[i - 1] + A[i - 1][1]
        S1[i] = S1[i - 1]

for i in B:
    tmp1 = S1[i[1]] - S1[i[0] - 1]
    tmp2 = S2[i[1]] - S2[i[0] - 1]
    print(tmp1, tmp2)
