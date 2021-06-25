A = list(map(int, input().split()))
Asum = sum(A)

for i in range(4):
    for j in range(i + 1, 4):
        if A[i] == Asum - A[i] or A[i] + A[j] == Asum - A[i] - A[j]:
            print("Yes")
            exit()

print("No")
