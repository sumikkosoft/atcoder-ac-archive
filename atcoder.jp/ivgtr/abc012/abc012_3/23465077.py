N = int(input())
tmp = 2025 - N

for i in range(1, 10):
    for j in range(1, 10):
        if i * j == tmp:
            print("{} x {}".format(i, j))
