N = int(input())

x = int((N // 1.08))

for i in range(x, x + 100):
    x = int(i * 1.08)
    if N == x:
        print(i)
        exit()
    elif N < x:
        print(":(")
        exit()

print(":(")
