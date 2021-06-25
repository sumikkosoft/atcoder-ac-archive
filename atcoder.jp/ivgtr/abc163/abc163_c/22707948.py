N = int(input())
A = list(map(int, input().split()))
tmp = {i: 0 for i in range(1, N + 1)}

for i in A:
    tmp[i] += 1

for i in tmp:
    print(tmp[i])
