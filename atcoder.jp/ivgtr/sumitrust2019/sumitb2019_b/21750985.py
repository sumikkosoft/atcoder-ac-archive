n = int(input())
x = int(n * (100 / 108))

for i in range(x - 10, x + 10):
    if int(i * (108 / 100)) == n:
        print(i)
        exit()

print(":(")
