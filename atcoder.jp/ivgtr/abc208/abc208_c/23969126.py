N, K = map(int, input().split())
A = list(map(int, input().split()))

B = sorted(A)
x = K % N
y = K // N
z = B[x - 1]

for i in A:
    if x == 0:
        print(y)
    elif i > z:
        print(y)
    else:
        print(y + 1)
