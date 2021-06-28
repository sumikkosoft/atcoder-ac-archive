N = int(input())
A = []
ans = 0

for i in range(N):
    t, L, R = map(int, input().split())
    if t == 1:
        A.append([L, R])
    elif t == 2:
        A.append([L, R - 0.5])
    elif t == 3:
        A.append([L + 0.5, R])
    elif t == 4:
        A.append([L + 0.5, R - 0.5])


for i in range(N):
    a, b = A[i]
    for j in range(i + 1, N):
        c, d = A[j]
        test1 = b < c
        test2 = d < a
        if not (test1 or test2):
            ans += 1

print(ans)
