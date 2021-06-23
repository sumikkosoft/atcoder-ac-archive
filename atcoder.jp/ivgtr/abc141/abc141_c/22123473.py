n, k, q = map(int, input().split())
a = [int(input()) for _ in range(q)]
b = [k - q for _ in range(n)]

for i in a:
    b[i - 1] += 1

for i in b:
    if i > 0:
        print("Yes")
    else:
        print("No")
