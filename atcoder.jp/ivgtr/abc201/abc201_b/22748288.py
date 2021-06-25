N = int(input())
tmp = list()

for i in range(N):
    a, b = input().split()
    tmp.append([a, int(b)])

tmp = sorted(tmp, key=lambda x: x[1])

print(tmp[-2][0])
