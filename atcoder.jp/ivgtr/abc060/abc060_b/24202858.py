A, B, C = map(int, input().split())
X = 10 ** 6 + 1

for i in range(1, X):
    if (B * i + C) % A == 0:
        print("YES")
        exit()

print("NO")
