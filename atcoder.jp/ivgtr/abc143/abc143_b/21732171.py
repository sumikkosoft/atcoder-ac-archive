a = int(input())
arr = list(map(int, input().split()))

m = 0
for i1 in range(a):
    for i2 in range(i1 + 1, a):
        m += arr[i1] * arr[i2]

print(m)
