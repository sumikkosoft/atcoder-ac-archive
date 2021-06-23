a, b = input().split()
A = 0
B = 0
for i in range(len(a)):
    A += int(a[i])
for i in range(len(b)):
    B += int(b[i])

print(max(A, B))
