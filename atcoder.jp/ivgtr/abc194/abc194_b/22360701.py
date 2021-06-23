n = int(input())
ans = float("inf")
A, B = [], []
flag = False
arr = list()
for i in range(n):
    a, b = map(int, input().split())
    ans = min(ans, a + b)
    A.append(a)
    B.append(b)

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        ans = min(max(A[i], B[j]), ans)


print(ans)
