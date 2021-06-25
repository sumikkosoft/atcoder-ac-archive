N = int(input())
A = dict()
tmp = list()

for _ in range(N):
    a, b = input().split()
    A[int(b)] = a
    tmp.append(int(b))

t = sorted(tmp)[-2]
print(A[t])
