N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
_B = []
C = list(map(int, input().split()))
_C = []
ans = 0

A.sort()
B.sort()
C.sort()

A_index = 0

for i in range(N):
    if A[A_index] < B[i]:
        _B.append(B[i])
        A_index += 1

B_index = 0
n = len(_B)

if n == 0:
    print(0)
    exit()

for i in range(N):
    if _B[B_index] < C[i]:
        _C.append(C[i])
        B_index += 1
        if B_index == n:
            break


print(len(_C))
