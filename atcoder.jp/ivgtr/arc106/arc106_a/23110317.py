N = int(input())
x = 37
y = 25

for i in range(1, x + 1):
    for j in range(1, y + 1):
        if 3 ** i + 5 ** j == N:
            print(i, j)
            exit()

print(-1)
