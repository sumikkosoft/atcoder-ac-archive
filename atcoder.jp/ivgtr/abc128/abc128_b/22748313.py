N = int(input())
tmp = list()

for i in range(N):
    a, b = input().split()
    tmp.append([i + 1, a, int(b)])

tmp = sorted(tmp, key=lambda x: x[2], reverse=True)
tmp = sorted(tmp, key=lambda x: x[1])

for i in tmp:
    print(i[0])
