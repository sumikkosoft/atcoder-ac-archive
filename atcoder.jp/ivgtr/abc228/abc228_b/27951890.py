N, X = map(int, input().split())
A = list(map(int, input().split()))

tmp = [False] * N

tmp[X - 1] = True
x = A[X - 1]

while not tmp[x - 1]:
    tmp[x - 1] = True
    x = A[x - 1]

print(sum(tmp))
