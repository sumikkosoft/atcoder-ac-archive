N = int(input())
tmp = [0] * N

for i in range(1, 101):
    for j in range(1, 101):
        for k in range(1, 101):
            x = (i + j + k) ** 2 - i * j - i * k - j * k
            if x <= N:
                tmp[x - 1] += 1

for i in range(N):
    print(tmp[i])
