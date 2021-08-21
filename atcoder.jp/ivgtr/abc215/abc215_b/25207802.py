N = int(input())
X = 1

while 2 ** X <= N:
    X += 1

print(X - 1)
