N = int(input())

MAX_N = 50000
t = 1.08

for i in range(MAX_N):
    x = int(i * t)
    if N == x:
        print(i)
        exit()
    elif N < x:
        print(":(")
        exit()


print(":(")
