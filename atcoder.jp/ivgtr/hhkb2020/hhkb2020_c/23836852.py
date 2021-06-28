N = int(input())
P = list(map(int, input().split()))

tmp = [0] * 200001
prev = 0

for i in range(N):
    tmp[P[i]] += 1
    while tmp[prev] != 0:
        prev += 1
    print(prev)
