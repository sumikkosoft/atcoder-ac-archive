n = int(input())

x = int(n * (100 / 108))

for i in range(x - 5, x + 5):
    if int(i * 1.08) == n:
        print(i)
        exit()

print(":(")
