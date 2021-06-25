N, M = map(int, input().split())
AC = [False] * N
WA = [0] * N
tmp = 0
for _ in range(M):
    A, B = input().split()
    if B == "AC" and not AC[int(A) - 1]:
        AC[int(A) - 1] = True
        tmp += WA[int(A) - 1]
    else:
        WA[int(A) - 1] += 1


print(AC.count(True), tmp)
